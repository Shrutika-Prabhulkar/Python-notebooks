def isPrimeFunc (num):
    #Set prime label
    isPrime = True

    #Check divisibility of given num
    for divisor in range (2, num-1):
        if num % divisor == 0:
             isPrime = False
             break

    #check the label
    if isPrime == True:
        print("Prime number")
    else:
        print("Non Prime number")    

num = eval(input("Enter the number "))
isPrimeFunc (num)
       