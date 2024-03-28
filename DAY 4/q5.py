# 5.Write a Python program that determines the largest of three numbers entered by the user.

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))

# chekch largest of three numbers entered by the user.
if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number is", largest)