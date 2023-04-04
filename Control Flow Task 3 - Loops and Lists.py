# Ctrl Flow Task 3 - Loops and Lists

# Loop with a range that says hello 10 times
repeat = range(10)

for i in repeat:
    print("Hello")

# Loop with a range that asks for names and appends to list_names

list_names = []

repeat = range(3)

for i in repeat:
    new_name = input("What is your name?\n")
    list_names.append(new_name)

print(list_names)

# Loop iterates over each name in list_name, and makes it lower case in new var called list_names_lower

list_names_lower = []

for names in list_names:
    names_lower = names.lower()
    list_names_lower.append(names_lower)

print(list_names_lower)

# Iterate over a list of values to find out if they are even

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in num_list:
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")

