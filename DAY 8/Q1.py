# 1. Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery”

# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert the sentence to lowercase and split it into words
words = sentence.lower().split()

# Create an empty dictionary to store the word counts
word_counts = {}

# Iterate over each word in the list
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_counts:
        word_counts[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        word_counts[word] = 1

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")