# Que 2: Python program to count the total number of digits in a number ?
#Example : n=123  digit=3

# input take from user

num = int(input("Enter a number : "))
# value = int(input("Enter a digit : "))
digit = 0
temp = num
while num > 0:
    num = int(num / 10)
    digit += 1
print("digit : ",digit)