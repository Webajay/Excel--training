# Que 4 : Write a function which returns the factorial of va number

def factorial_naive(n):

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Example usage:
number = 5
result = factorial_naive(number)
print(f"The factorial of {number} is: {result}")
