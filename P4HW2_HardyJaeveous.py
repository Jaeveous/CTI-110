#Jaeveous Hardy
#July 7, 2024
#P4HW2
#Employee pay chart Update

employee = print(input("Enter employee's name: "))

hours_worked = int(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))
pay = hours_worked * pay_rate

overTime = hours_worked - 40
overTime_pay = 1.25 * pay_rate
reghour = hours_worked * pay_rate
gross_pay = hours_worked * pay_rate + overTime_pay


print('-------------------------------------')

print('Employee name:',employee)
print()


print('Hours Worked    Pay Rate    OverTime    OverTime Pay    Regular Pay    Gross Pay')
print('--------------------------------------------------------------------------------')
print(f'{hours_worked:<15.2f} {pay_rate:<11.2f} {overTime:<11.2f} {overTime_pay:<15.2f} {reghour:<14.2f} {gross_pay:.2f}')



employee2 = print(input("Enter employee's name or 'Done' to terminate: "))
if employee2 == 'Done':
    print('Program Over')
else:
    hours_worked2 = int(input('Enter number of hours worked: '))
    pay_rate2 = float(input("Enter employee's pay rate: "))
        
pay2 = hours_worked * pay_rate
overTime2 = hours_worked - 40
overTime_pay2 = 1.25 * pay_rate
reghour2 = hours_worked * pay_rate
gross_pay2 = hours_worked * pay_rate + overTime_pay


print('--------------------------------------')

print('Employee name:',employee2)
print()


print('Hours Worked    Pay Rate    OverTime    OverTime Pay    Regular Pay    Gross Pay')
print('--------------------------------------------------------------------------------')
print(f'{hours_worked2:<15.2f} {pay_rate2:<11.2f} {overTime2:<11.2f} {overTime_pay2:<15.2f} {reghour2:<14.2f} {gross_pay2:.2f}')

print()
print()



print("Total nnumer of empoyee's entered: 2")
print('Total amount paid for overtime:', overTime_pay + overTime_pay2)
print('Total amount for reular hours:', reghour + reghour2)
print('Total amount in gross:', gross_pay + gross_pay2)

 






