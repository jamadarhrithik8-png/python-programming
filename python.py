name = input("Enter student name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
usn = input("Enter USN number: ")
department = input("Enter department: ")

marks = []
for i in range(1, 6):
    m = float(input("Enter marks of subject " + str(i) + ": "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

if percentage >= 75:
    message = "Distinction"
elif percentage >= 60:
    message = "First Class"
elif percentage >= 50:
    message = "Second Class"
elif percentage >= 35:
    message = "Pass"
else:
    message = "Fail"

print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("DOB:", dob)
print("USN:", usn)
print("Department:", department)
print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Result:", message)
