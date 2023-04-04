# Ctrl Flow Task 3 - Loops and Lists


# Loop with a range that says hello 10 times

```commandline
repeat = range(10)

for i in repeat:
    print("Hello")
```
The output would look like this:
```commandline
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
```
# Loop with a range that asks for names and appends to list_names

We must initialise a list first.

`list_names = []`

We now create a `range` with 3 elements and assign it to `repeat`
The `for` loop allows us to iterate each element within the `range`.
```
repeat = range(3)

for i in repeat:
    new_name = input("What is your name?\n")
    list_names.append(new_name)

print(list_names)
```
Once the input is taken, it will add to the new `list_names` due to the use of `.append`, and the new list will be printed out.

The output is as such:
```
What is your name?
Mohammad
What is your name?
Hussain
What is your name?
Michael
['Mohammad', 'Hussain', 'Michael']
```
# Loop iterates over each name in list_name, and makes it lower case in new list called list_names_lower
```commandline
list_names_lower = []

for names in list_names:
    names_lower = names.lower()
    list_names_lower.append(names_lower)

print(list_names_lower)
```
Output:

`['mohammad', 'hussain', 'michael']`

# Iterate over a list of values to find out if they are even
```commandline
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in num_list:
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")
```
Number list is created with numbers from 1 to 10, using the `for` loop, we define `num` as the elements within the list.
Using the `if` statement coupled with the modulo `%`, it allows us to evaluate the list to detecting the odd and even numbers and printing when so.