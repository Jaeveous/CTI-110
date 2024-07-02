#Jaeveous Hardy
#July 1, 2024
#P3H1_Debug
#Fixing a programm

grade_list = [ ]

module1= float(input("Enter grade for Module 1 "))
grade_list.append(module1)

module2= float(input("Enter grade for Module 2 "))
grade_list.append(module2)

module3= float(input("Enter grade for Module 3 "))
grade_list.append(module3)

module4= float(input("Enter grade for Module 4 "))
grade_list.append(module4)

module5= float(input("Enter grade for Module 5 "))
grade_list.append(module5)

module6= float(input("Enter grade for Module 6 "))
grade_list.append(module6)
print()
print('-------------Results------------')


min_val = min(grade_list)
max_val = max(grade_list)
sum_val = sum(grade_list)
avg_val = sum_val/6




print(f'Lowest Grade: {min_val: .2f}')
print(f'Highest Grade: {max_val: .2f}')
print(f'Sum of Grades: {sum_val: .2f}')
print(f'Average: {avg_val: .2f}')
print('--------------------------------')


if avg_val>=90:
    letter_grade = 'A'
     
elif avg_val >= 80:
    letter_grade = "B"
elif avg_val>=70:
    letter_grade = "C"
elif avg_val>=60:
    letter_grade = "D"
     
else:
     letter_grade = "F"

print('Your grade is:', letter_grade)
