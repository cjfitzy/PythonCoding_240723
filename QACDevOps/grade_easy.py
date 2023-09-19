maths_mark = int(input("Enter your maths mark out of 100:"))
chem_mark = int(input("Enter your chemistry mark out of 100:"))
physics_mark = int(input("Enter your physics mark out of 100:"))

total_marks = maths_mark + chem_mark + physics_mark

percentage = (total_marks/300)*100

if percentage < 40:
    grade = "You failed"
elif percentage >= 40 and percentage < 50:
    grade = "D"
elif percentage >= 50 and percentage <60:
    grade = "C"
elif percentage >= 60 and percentage <70:
    grade = "B"
else:
    grade = "A"

print("Your percentage score is:",percentage)
print("You scored a grade of:", grade)