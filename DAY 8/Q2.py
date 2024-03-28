#2.Write a Python program to remove a newline  in PythonString = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters using replace()
new_string = string.replace("\n", "")

print(new_string)

my_string = "\nBest \nDeeptech \nPython \nTraining\n"
new_string = "".join(map(str.strip, my_string.split("\n")))

print(new_string)

string = "Hello world! \n\n"

# Remove only trailing newline characters
new_string = string.rstrip()

print(new_string)