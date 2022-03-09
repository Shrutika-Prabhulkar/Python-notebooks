def sum_num(start,end):
    total = 0
    for num in range(start,end):
        total = total + num
        num = num + 1
    print("Sum is ",total)    

sum_num(1,11) 
sum_num(20,40)  
sum_num(50,100)     