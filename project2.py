import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

guess = None
guess_count = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while guess != target_number:
    try:
        guess = int(input("Enter your guess: "))
        guess_count += 1

        if guess > target_number:
            print("Lower number please")
        elif guess < target_number:
            print("Higher number please")
        else:
            print(f"Congratulations! You guessed the number in {guess_count} attempts.")
    except ValueError:
        print("Please enter a valid integer!")
