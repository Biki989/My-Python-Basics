n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    if(i == 1 or i == n):                 # first or last row
        print("*" * n, end="")            # full line of stars
    else:                                 # middle rows
        print("*", end="")                # left border star
        print(" " * (n-2), end="")        # spaces in between
        print("*", end="")                # right border star
    print("")                             # move to next line


# n = int(input("Enter the number of rows: "))

# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")
