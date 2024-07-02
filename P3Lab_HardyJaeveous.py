
#Jaeveous Hardy
#July 1, 2024
#P3Lab
#Exact Change



money = float(input('Enter the amount of money as a float: '))
#Convert to cents

cents = int(money / .01)

#Convert to Dollars

numDollars = cents//100
centsLeft = cents%100

numQuarters = centsLeft//25
centsLeft = centsLeft%25

numDimes = centsLeft//10
centsLeft = centsLeft%10

numNickel = centsLeft//5
centsLeft = centsLeft%5

if(cents == 0):
    print('No Change')

if(numDollars == 1):
    print(numDollars, "Dollar")
    
else:
    (numDollars>0)
    print(numDollars, "Dolllars")



if(numQuarters == 1):
    print(numQuarters, "Quarter")
    
else:
    (numQuarters>0)
    print(numQuarters, "Quarters")


if(numDimes == 1):
    print(numDimes, "Dime")
    
else:
    (numDimes>0)
    print(numDimes, "Dimes")




if(numNickel == 1):
    print(numNickel, "Nickel")
    
else:
    (numNickel>0)
    print(numNickel, "Nickels")
 

if(centsLeft == 1):
    print(centsLeft, "Penny")
    
else:
    (centsLeft>0)
    print(centsLeft, "Pennies")
   

