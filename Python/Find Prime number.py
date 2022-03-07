#Prompt the user to enter number
num = eval(input("Enter the number "))

#Check the divisibility of the given number
count = 0
for divisor in range(1, num+1):
    if num % divisor == 0:
        count = count +1

if count == 2:
    print("Prime number")
else:
    print("Non prime number")    
