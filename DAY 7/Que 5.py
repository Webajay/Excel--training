# Que 5: Python program to get the Fibonacci series between 0 to 50.

# Initialize variables
a, b = 0, 1

# Print Fibonacci series up to 50
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b