#Prompt the user to enter number
num = eval(input("Enter the number "))

# check for divisibility of a number from 1 to given number
for divisor in range(1,num+1):
#if divisible then print the number
    if num % divisor ==0:
        print(divisor)
   