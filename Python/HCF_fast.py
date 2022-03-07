#Find the Highest common factor

#Prompt the user to enter 2 numbers
num1 , num2 = eval(input("Enter 2 numbers separated by ,: "))

#Compute
rem = num1 % num2
while rem !=0:
    num1 , num2 = num2, rem
    rem = num1 % num2
#Display result
print("HCF is ",num2)