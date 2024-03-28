# Que 1: Write a program to calculate the sum of the odd numbers within the given range ?

# input take from user

Start = int(input("Enter Start Range : "))
Stop = int(input("Enter Stop Range : "))

sum = 0
for i in range(Start, Stop + 1):
    if i % 2 != 0:
        print(i)
        sum += 1
print("Sum of Odd number : "+str(sum))