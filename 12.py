p=int(input("Enter your number:"))
if p<0:
    print("The number is not a natural number")
else:
    t=0
    for i in range (0,p+1):
        t+=i
print("The sum is:", t)