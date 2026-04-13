# List of names
name_list = ["Alice", "Bob", "Charlie", "Biki", "David"]

# Get the name from user
name = input("Enter the name to search: ")

# Check if the name is in the list
if name in name_list:
    print("The name is present in the list.")
else:
    print("The name is NOT present in the list.")
