#HiFive_HiEven
#Prompt the user to enter an integer
inte_num = eval(input("Enter an integer"))

#Compute the number divisible by 5
if inte_num % 5 ==0:
    print("HiFive")

#Compute the number divisible by 2
if inte_num % 2 ==0:
    print("HiEven")

print('Program executed')