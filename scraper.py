from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
import re

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
REQUEST_TIMEOUT = 10
SLEEP_TIME = 3
MAX_RETRIES = 3

def get_html_static(url):
    headers = {"User-Agent": USER_AGENT}
    for _ in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            time.sleep(1)
    return None

def get_html_dynamic(url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument(f"user-agent={USER_AGENT}")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    driver.quit()
    return html

def scrape_single_page(url, keyword):
    html = get_html_static(url)
    soup = BeautifulSoup(html, "html.parser") if html else None

    if not soup or keyword.lower() not in soup.get_text().lower():
        html = get_html_dynamic(url)
        soup = BeautifulSoup(html, "html.parser")

    data = []
    for link in soup.find_all("a", href=True):
        text = link.get_text(strip=True)
        href = link.get("href")

        # Clean title text
        if not text or len(text) < 4:
            continue

        # Skip irrelevant links
        if any(skip in href for skip in ["facebook", "twitter", "instagram", "#", "mailto:"]):
            continue

        if keyword.lower() in text.lower():
            full_url = urljoin(url, href)
            clean_title = re.sub(r'\s+', ' ', text).strip()
            data.append({"Title": clean_title, "Link": full_url})
    return data

def detect_next_page(soup):
    next_link = soup.find("a", string=re.compile("next", re.IGNORECASE))
    if next_link and next_link.get("href"):
        return next_link.get("href")
    return None

def scrape_all_pages(start_url, keyword):
    all_results = []
    current_url = start_url
    page_num = 1

    while current_url:
        print(f"📄 Scraping page {page_num} → {current_url}")
        html = get_html_static(current_url)
        soup = BeautifulSoup(html, "html.parser") if html else None
        if not soup or keyword.lower() not in soup.get_text().lower():
            html = get_html_dynamic(current_url)
            soup = BeautifulSoup(html, "html.parser")

        page_data = scrape_single_page(current_url, keyword)
        if not page_data:
            break
        all_results.extend(page_data)

        next_url = detect_next_page(soup)
        if next_url and not next_url.startswith("http"):
            current_url = urljoin(current_url, next_url)
        else:
            current_url = next_url
        page_num += 1

    return all_results

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    
    # Remove 'Link' column before saving
    if "Link" in df.columns:
        df = df.drop(columns=["Link"])
    
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Scraped Data")
    try:
        os.startfile(filename)
    except AttributeError:
        print(f"📂 File saved: {filename} (open manually)")


if __name__ == "__main__":
    keyword = input("Enter keyword: ").strip()
    website = input("Enter starting URL: ").strip()
    auto_paginate = input("Auto-detect next pages? (y/n): ").strip().lower() == 'y'

    if auto_paginate:
        results = scrape_all_pages(website, keyword)
    else:
        start_page = int(input("Enter start page number: ").strip())
        end_page = int(input("Enter end page number: ").strip())
        results = []
        for page_num in range(start_page, end_page + 1):
            url = website.format(page=page_num) if "{page}" in website else f"{website}?page={page_num}"
            results.extend(scrape_single_page(url, keyword))

    if results:
        # Add timestamp so file is always unique
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"scraped_{keyword}_{timestamp}.xlsx"
        
        save_to_excel(results, filename)
        print(f"✅ Saved {len(results)} results to {filename}")
    else:
        print("❌ No results found.")