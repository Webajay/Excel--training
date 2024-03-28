# Take input from the user for the first number
num1 = float(input("Enter the first number: "))

# Take input from the user for the second number
num2 = float(input("Enter the second number: "))

# Display the original numbers
print("Original numbers:", num1, "and", num2)

# Swap the numbers
num1, num2 = num2, num1

# Display the swapped numbers
print("Swapped numbers:", num1, "and", num2)
