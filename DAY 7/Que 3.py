# Que 3:  Python program to check if the given string is a palindrome.

# input take by a user
x = str(input("Enter any palindrome:"))

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")