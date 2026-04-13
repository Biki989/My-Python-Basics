a1= float(input("Enter a number: "))
a2= float(input("Enter another number: "))
a3= float(input("Enter another number: "))
a4= float(input("Enter another number: "))
if a1 > a2 and a1 > a3 and a1 > a4:
    print("The largest number is:", a1)
elif a2 > a3 and a2 > a4:
    print("The largest number is:", a2)
elif a3 > a4:
    print("The largest number is:", a3)
else:
    print("The largest number is:", a4)