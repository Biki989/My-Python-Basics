# Get marks from the user
marks = float(input("Enter your marks (0 - 100): "))

if marks >= 90:
        grade = "Ex"
elif marks >= 80:
        grade = "A"
elif marks >= 70:
        grade = "B"
elif marks >= 60:
        grade = "C"
elif marks >= 50:
        grade = "D"
else:
        grade = "F"

print(f"Your grade is: {grade}")

# # Get marks from the user
# marks = float(input("Enter your marks (0 - 100): "))

# # Check for valid range
# if marks < 0 or marks > 100:
#     print("Invalid marks. Please enter a value between 0 and 100.")
# else:
#     # Determine grade
#     if marks >= 90:
#         grade = "Ex"
#     elif marks >= 80:
#         grade = "A"
#     elif marks >= 70:
#         grade = "B"
#     elif marks >= 60:
#         grade = "C"
#     elif marks >= 50:
#         grade = "D"
#     else:
#         grade = "F"

#     print(f"Your grade is: {grade}")

