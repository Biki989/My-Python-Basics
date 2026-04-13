marks1=float(input("enter marks1: "))
marks2=float(input("enter marks1: "))
marks3=float(input("enter marks1: "))
sum= marks1+marks2+marks3
print(f'the total sum is:{sum}')
percentage= sum/3
print(f'total percentage:{percentage:.2f}')
if (marks1>33 and marks2>33 and marks3>33 and sum/3>40):
    print('the student has passed')
else:
    print('the student has failed')        
#     # Input marks for 3 subjects
# marks1 = float(input("Enter marks for subject 1: "))
# marks2 = float(input("Enter marks for subject 2: "))
# marks3 = float(input("Enter marks for subject 3: "))

# # Calculate total and percentage
# total = marks1 + marks2 + marks3
# percentage = total / 3

# # Display results
# print(f"Total marks: {total}")

# print(f"Percentage: {percentage:.2f}%")

# # Check pass/fail conditions
# if marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and percentage >= 40:
#     print("The student has passed.")
# else:
#     print("The student has failed.")