# 3. Write a Python program to reverse words in astringString = “Deeptech Python Training”


string = "Deeptech Python Training"

# Split the string into words and reverse the order of the words
reversed_words = string.split()[::-1]

# Join the reversed words into a string with spaces between them
reversed_string = " ".join(reversed_words)

print(reversed_string)

string = "Deeptech Python Training"

# Split the string into words and reverse the order of the words using list comprehension
reversed_words = [word[::-1] for word in string.split()[::-1]]

# Join the reversed words into a string with spaces between them
reversed_string = " ".join(reversed_words)

print(reversed_string)