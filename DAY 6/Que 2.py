# Que 2: Write a program to print all even number from a given range ?

# input take from user

Start = int(input("Enter a Start Number : "))
End = int(input("Enter a End Number : "))

while Start <= End:
    if Start % 2 == 0:
        print(Start)
    Start += 1