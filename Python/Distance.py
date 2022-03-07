# prompt the user to enter 1st point co ordinates
x1, y1 = eval(input("Enter x1, y1 -"))

#prompt the user to enter 2nd point co ordinates
x2, y2 = eval(input("Enter x2, y2 -"))

#compute the ecludian distance
distance = ((x2 - x1) ** 2 + (y2 - y1)** 2) ** 0.5

# display the distance
print("Distance is ",distance)
