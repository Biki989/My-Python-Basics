# def print_pattern(n):
#     for i in range(n, 0, -1):
#         print('*' * i)

# # Example usage:
# lines = int(input("Enter number of lines: "))
# print_pattern(lines)
def print_pattern(n):
    if n == 0:
        return
    print('*' * n)
    print_pattern(n - 1)

# Example usage:
lines = int(input("Enter number of lines: "))
print_pattern(lines)
