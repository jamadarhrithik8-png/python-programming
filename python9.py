name=input("Enter your name: ")
Birth_year=int(input("Enter your birth year: "))
current_year=2026
age=current_year-Birth_year
if age>=60:
    print("senior citizen")
else:
    print("not a senior citizen")