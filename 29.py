
import os

def generateTable(n):
    os.makedirs("table", exist_ok=True)     # create folder if not exists
    
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"

    with open(f"table/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
