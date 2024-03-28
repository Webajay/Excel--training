# Que 5: Write a program to calculate the sum of the first n natural numbers ?

# input take from user

num = int(input("Enter a number : "))

n = 0
i = 1

while i <= num:
    n = n+i
    i += 1
    print("The Sum is : ",n)