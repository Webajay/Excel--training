# Que 6: Write a program to calculate the sum of the first n natural numbers ?

# input take from user

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


# Driver Code
num = int(input("Enter the number:"))
print("Factorial of", num, "is", factorial(num))