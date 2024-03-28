# Write a program to calculate the area of a circle, triangle, rectangle and square

import math

print("**********Choose an Option:********* ")
print("1: Area of the Circle")
print("2: Area of the Rectangle ")
print("3: Area of the Triangle ")
print("4: Area of the Square ")

# input the desired shape
choice = int(input("plese choice an option:"))

# area of a circle
if choice==1:
    # input circle radius
    radius = float(input("Enter the radius of the Circle: "))
    area = math.pi*pow(radius,2)
    print(f"The area of the circle with radius {radius} is : {round(area,2)}")

#area of a rectangle
elif choice==2:
    width =float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))
    area = width*length
    print(f"The area of the rectangle is {round(area,2)}")

# area of a triangle using Heron's formula
elif choice ==3:
    a, b , c = map(float, input("Enter the 3 sides of triangle eg (12 13 14):").split())
    s= (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"The area of the triangle is {round(area,2)}")

#area of a Square
elif choice ==4:
    side =float(input("Enter the side of the square: "))
    area = side*side
    print(f"The area of the square is {round(area,2)}")

else: 
    print("Wrong Choice")