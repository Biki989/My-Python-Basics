# Program to check if the word 'twinkle' is in the file 'poems.txt'

file = open('poems.txt', 'r')        # Open the file in read mode
content = file.read().lower()        # Read the whole content and convert to lowercase
file.close()                         # Close the file

if 'twinkle' in content:
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is NOT present in the file.")
