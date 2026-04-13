
import tkinter as tk
import random

# Mapping choices
choices = {"Snake": 1, "Water": -1, "Gun": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

# Game logic
def play(user_choice):
    user = choices[user_choice]
    computer = random.choice([-1, 0, 1])

    result_text = f"You chose: {user_choice}\nComputer chose: {reverse[computer]}\n"

    if user == computer:
        result_text += "It's a draw!"
    elif (computer == -1 and user == 1) or \
         (computer == 1 and user == 0) or \
         (computer == 0 and user == -1):
        result_text += "You win!"
    else:
        result_text += "You lose!"

    result_label.config(text=result_text)

# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("300x350")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Snake - Water - Gun", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

snake_btn = tk.Button(button_frame, text="Snake", width=10, command=lambda: play("Snake"))
snake_btn.grid(row=0, column=0, padx=5)

water_btn = tk.Button(button_frame, text="Water", width=10, command=lambda: play("Water"))
water_btn.grid(row=0, column=1, padx=5)

gun_btn = tk.Button(button_frame, text="Gun", width=10, command=lambda: play("Gun"))
gun_btn.grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=250, justify="center")
result_label.pack(pady=20)

# Run the app
root.mainloop()