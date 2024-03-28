# Que 4: Python program to count the number of even and odd numbers from a series of numbers. [3,776,46,22,63,59,19,44,676]

# list of numbers
list1 = [3,776,46,22,63,59,19,44,676]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)