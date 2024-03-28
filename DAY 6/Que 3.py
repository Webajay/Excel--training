# Que 3: Write a program to check whether  a number is prime or not ?

# input take from user

num = int(input("Enter a NUmber : "))
i = 2
f = 1
while i <= num/2:
    if num % i == 0:
        f = 0
        break
    i += 1

if f == 0:
    print("Not a Prime")
else:
    print("Prime")