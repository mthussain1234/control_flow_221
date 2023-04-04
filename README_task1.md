## Movie Ratings

To ask the user for their age, and to allow for the input we use the following code:
```commandline
print("Welcome to the cinema. Please enter your age: ")

customer_age = int(input())
```
We must input a line where it addresses invalid ages. User will be met with a printed message to re-enter their age.
```commandline
if customer_age < 1 or customer_age > 117:
    print("Invalid Age! Please enter your correct age!")
```
Depending on the age they enter, they will get a printed message back saying which movies they are eligible to watch.

```commandline
elif customer_age < 18:
    print("You can watch movies rated U, PG, 12, 15")
elif customer_age < 15:
    print("You can watch movies rated U, PG, 12")
elif customer_age < 12 :
    print("You can watch movies rated U, PG")
```
We finally need our `else` function to cover all ages above 18, and print a message to allow them to watch any movie available.

`else:
    print("You can watch all the available movies!")`

# OPTIONAL

Using the `.isdigit` method, it will return True if all the characters are digits, otherwise False.

Casting this over the pre-existing code as shown above, and adding one more else statement at the end to allow for the break, lets us detect string entries and allow for us to respond to them.

```commandline
print("Welcome to the cinema. Please enter your age: ")

customer_age = input()
if customer_age.isdigit():
    if customer_age < 1 or customer_age > 117:
        print("Invalid Age! Please enter your correct age!")
    elif customer_age < 18:
        print("You can watch movies rated U, PG, 12, 15")
    elif customer_age < 15:
        print("You can watch movies rated U, PG, 12")
    elif customer_age < 12 :
        print("You can watch movies rated U, PG")
    else:
        print("You can watch all the available movies!")
else:
    print("Invalid Input! Please enter a valid age.")

```