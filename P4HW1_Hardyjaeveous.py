#Jaeveous Hardy
#July 7, 2024
#P4HW1
#Storing Grades
#Ask user to enter grades

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


print(f'Lowest Grade: {min_val:.2f}')
print(f'Highest Grade: {max_val:.2f}')
print(f'Sum of Grades: {sum_val:.2f}')
print(f'Average: {avg_val:.2f}')
print('--------------------------------')
#ask user how many score do the want to enter

score_list = []

user = int(input('How many score do you want to enter?: '))


if user == 1:
    score1 = int(input('Enter score #1: '))
    score_list.append(score1)
    

    
if user == 2:
    score1 = int(input('Enter score #1 '))
    score_list.append(score1)
    
    score2 = int(input('Enter score #2 '))
    score_list.append(score2)

    

if user == 3:
    score1 = int(input('Enter score #1 '))
    score_list.append(score1)
    
    score2 = int(input('Enter score #2 '))
    score_list.append(score2)
    
    score3 = int(input('Enter score #3 '))
    score_list.append(score3)

if user == 4:
    score1 = int(input('Enter score #1 '))
    score_list.append(score1)
    
    score2 = int(input('Enter score #2 '))
    score_list.append(score2)
    
    score3 = int(input('Enter score #3 '))
    score_list.append(score3)
    
    score4 = int(input('Enter score #4 '))
    score_list.append(score4)

if user == 5:
    score1 = int(input('Enter score #1 '))
    score_list.append(score1)
    
    score2 = int(input('Enter score #2 '))
    score_list.append(score2)
    
    score3 = int(input('Enter score #3 '))
    score_list.append(score3)
    
    score4 = int(input('Enter score #4 '))
    score_list.append(score4)
    
    score5 = int(input('Enter score #5 '))
    score_list.append(score5)


if user == 6:
    score1 = int(input('Enter score #1 '))
    score_list.append(score1)
    
    score2 = int(input('Enter score #2 '))
    score_list.append(score2)
    
    score3 = int(input('Enter score #3 '))
    score_list.append(score3)
    
    score4 = int(input('Enter score #4 '))
    score_list.append(score4)
    
    score5 = int(input('Enter score #5 '))
    score_list.append(score5)
    
    score6 = int(input('Enter score #6 '))
    score_list.append(score6)

print('----------Results----------')

smin_val = min(score_list)
smax_val = max(score_list)
ssum_val = sum(score_list)
savg_val = sum_val/6


print(f'Lowest Score: {smin_val:.2f}')
score_list.remove(smin_val)

print('Modified List:', score_list)
print('Scores Average:', savg_val)

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

print('Grade:', letter_grade)






        



