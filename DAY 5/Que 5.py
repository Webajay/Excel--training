# Que 5 : Write a function which prints number of alphabets in a string

def count_alphabets(s):
    # Initialize a variable to keep count of alphabets
    alphabets_count = 0

    # Iterate through each character in the string
    for char in s:
        if char.isalpha():
            alphabets_count += 1

    # Print the count of alphabets
    print("Number of alphabets in the given string: ", alphabets_count)

# Test the function
count_alphabets("Hello, World!")