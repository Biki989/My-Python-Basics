class MyClass:
    a = 10  # Class attribute

# Create an object
obj = MyClass()

# Print class and object attribute initially
print("Before changing:")
print(f"Class attribute: {MyClass.a}")
print("Object attribute:", obj.a)

# Now change 'a' using the object
obj.a = 0

print("\nAfter changing obj.a = 0:")
print("Class attribute:", MyClass.a)
print("Object attribute:", obj.a)
