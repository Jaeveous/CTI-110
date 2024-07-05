#Jaeveous Hardy
#July 4, 2024
#P3HW2
#Employee pay chart

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



