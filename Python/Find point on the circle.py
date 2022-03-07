#Find point on the circle
#Prompt the user to enter 1st point co ordinates
x1 , y1 = eval(input("Enter center co-ordinates of  x1 ,y1 - "))

#Prompt the user to enter radius of circle
radius = eval(input("Enter radius of circle "))

#Prompt the user to enter co ordinates of point
x2 , y2 = eval(input("Enter point co ordinates of x2, y2 "))

#Compute the distance between center & point
distance = ((x2 - x1)** 2 + (y2 - y1)** 2)** 0.5

if distance > radius:
    print("Outside the circle")
elif distance < radius:
    print("Inside the circle")
else :
    print("On the circle")        