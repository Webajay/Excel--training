# 4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training”


# Initialize the vowels as a string
vowels = "aeiouAEIOU"

# Given string
string = "Welcome to python Training"

# Intialize the vowel count as 0
vowel_count = 0

# Traverse the string
for char in string:

    # Check if the character is in the vowels
    if char in vowels:

        # Increment the vowel count
        vowel_count += 1

# Print the vowel count
print("Vowel count: ", vowel_count)

# Print the list of vowels
vowels_list = [char for char in string if char in vowels]
print("Vowels: ", vowels_list)