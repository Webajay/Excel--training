# Que 1 : Write a function to calculate number of primes in a range.

def count_primes(start, end):
    flag = 0  # Declaring flag variable
    count = 0  # Declaring prime number counter

# elements range between starting and ending range
    for i in range(start, end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, i):
                if (i % j == 0):
                    flag = 1
                    break
                else:
                    flag = 0
            if (flag == 0):
                count += 1
    return count

# inpute taken by the user
st = int(input("Enter the start value : "))
ed = int(input("Enter the End value : "))

# Test the function
start = st
end = ed
print("The number of primes in this range are: ", count_primes(start, end))