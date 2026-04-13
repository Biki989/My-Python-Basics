# Ask the user to enter a username
username = input("Enter your username: ")

# Check length of username
if len(username) < 10:
    print("The username has less than 10 characters.")
else:
    print("The username has 10 or more characters.")
