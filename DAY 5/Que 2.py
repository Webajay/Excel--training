# Que 2 : Write a function which Checks whether a numer is even or odd.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
num = int(input("Enter a number: "))
print(f"The number is {check_even_odd(num)}.")
