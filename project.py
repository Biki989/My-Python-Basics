import time
import random

name = input("Enter your name: ")
print(f"Hi!! We'll play a game of arithmetic today, are you ready {name}?")
time.sleep(1)

print("Let's start!!")
time.sleep(1)

print("We'll choose an operator for you from these: +, -, *, /")
time.sleep(1.2)

operators = ['+', '-', '*', '/']
chosen_operator = random.choice(operators)

num1 = random.randint(-10000, 10000)
print('The first number is', num1)
time.sleep(1)

num2 = random.randint(-10000, 10000)
print('The second number is', num2)
time.sleep(1)

match chosen_operator:
    case '+':
        print("Do addition (+)")
    case '-':
        print("Do subtraction (-)")
    case '*':
        print("Do multiplication (×)")
    case '/':
        print("Do division (/)")
time.sleep(1)

print('Answer it in one minute ⏱️')
for i in range(60, 0, -1):
    print(f"Time left: {i} seconds")
    time.sleep(1)

print("⏰ Time's up!")

if chosen_operator=='+':
    print(f"The addition of these two numbers are :{num1+num2}")
elif chosen_operator=='-':
    print("The subtraction of the two numbers are:",num1-num2)        
elif chosen_operator=='*':
    print("The multiplication of the two numbers are:",num1*num2)        
elif chosen_operator=='-':
    print("The division of the two numbers are:",num1/num2)        