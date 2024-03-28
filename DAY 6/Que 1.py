# Que 1: Write a program to calculate power of a number. Input number and its exponents from user ?

# input take from user

num = int(input("Enter a number : "))
exp = int(input("Enter its Power : "))

i = 1
result = 1
while i <= exp:
    result = result*num
    i += 1

print("Result : "+str(result))