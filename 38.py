class Animals:
    def __init__(self, name):
        self.name = name


class Pets(Animals):
    def __init__(self, name, owner):
        super().__init__(name)  # Call parent constructor
        self.owner = owner


class Dog(Pets):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example usage
my_dog = Dog("Buddy", "Alice", "Golden Retriever")
print(f"Dog's Name: {my_dog.name}")
print(f"Owner: {my_dog.owner}")
print(f"Breed: {my_dog.breed}")
my_dog.bark()
