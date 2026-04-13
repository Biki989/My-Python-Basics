# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.
# class programmer():
#     name="biki"
#     salary=120000
#     language="python"
# biki=programmer()    
# print(biki.name,biki.salary)
class Programmer:
    company = "Microsoft"  # Class variable (common to all programmers)

    def __init__(self, name, age, language, position):
        self.name = name
        self.age = age
        self.language = language
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Language: {self.language}")
        print(f"Position: {self.position}")
        print(f"Company: {Programmer.company}")
        print("-" * 30)


# Creating objects of Programmer class
p1 = Programmer("Alice", 28, "Python", "Software Engineer")
p2 = Programmer("Bob", 32, "C++", "Senior Developer")
p3 = Programmer("Charlie", 25, "JavaScript", "Frontend Developer")

# Displaying their information
p1.display_info()
p2.display_info()
p3.display_info()