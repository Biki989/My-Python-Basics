def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
# def print_table(n, i=1):
#     if i > 10:
#         return
#     print(f"{n} x {i} = {n * i}")
#     print_table(n, i + 1)
print_table(6)
