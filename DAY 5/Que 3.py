# Que 3 : Write a function which returns the sum of n natural Numbers

def sum_of_natural_numbers_while(n):

    if n < 0:
        print("Enter a positive number")
    else:
        total = 0
        while n > 0:
            total += n
            n -= 1
        return total

# Example usage:
n = 16
result_while = sum_of_natural_numbers_while(n)
print(f"The sum of the first {n} natural numbers (using while loop) is {result_while}")
