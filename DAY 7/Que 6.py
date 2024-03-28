# Que 6:  Python program that accepts a string and calculates the number of digits special chars and alphabets.

def count_chars(string):
    num_digits = num_special_chars = num_alphabets = 0

    for char in string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_alphabets += 1
        else:
            num_special_chars += 1

    return num_digits, num_special_chars, num_alphabets


input_string = input("Enter a string: ")

digits, special_chars, alphabets = count_chars(input_string)

print("Number of digits:", digits)
print("Number of special characters:", special_chars)
print("Number of alphabets:", alphabets)