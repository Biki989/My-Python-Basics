p=int(input("Enter your number:"))
if(p<0):
    print('This is not a natural number')
else:
    t=1
    for i in range (1,p+1):
        t*=i
        print(f'The factorial for {i} step is {t}')
    print("The factorial is:", t)