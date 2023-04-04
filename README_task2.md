# Odd or Even

This program asks the user for a number.
If the number is odd, the program will print if it is odd and the same with even numbers.

We need a print statement to prompt the user to enter a number, and also an input function to allow the number to be inputted.

```commandline
print("Please input any number!")
num1 = int(input())
```
We will now use an if and else statement, along with a modulo to check if the number inputted is even or odd.
```commandline
if (num1 % 2) == 0:
    print("The number you have picked is even")
else:
    print("The number you have picked is odd")
```

# Higher or Lower

To start off we must import the random library we do this by:

`import random`

After importing this, we must define the correct answer to a randomized value between 1 and 20.
`correct_answer = random.randint(1, 20)`

After this we print the welcome message telling the user to start guessing, and also some code to allow for input.

```commandline
print("Guess a number between 1 and 20. You have 3 guesses")

num1 = int(input())
```
We now need to use our `if` `elif` `else` statements to print out messages if the guess is correct, higher or lower.
```commandline
if num1 == correct_answer:
    print("You are correct!")
elif num1 > correct_answer:
    print("Your guess is too high. You have 2 guesses left.")
else:
    print("Your guess is too low. You have 2 guesses left.")
```
This is repeated 2 more times to allow for the 3 guesses.
```
num2 = int(input())

if num2 == correct_answer:
    print("You are correct!")
elif num2 > correct_answer:
    print("Your guess is too high. You have 1 guess left.")
else:
    print("Your guess is too low. You have 1 guess left.")

num3 = int(input())

if num3 == correct_answer:
    print("You are correct!")
elif num3 > correct_answer:
    print("Your guess is too high. Better luck next time!")
else:
    print("Your guess is too low. Better luck next time!")
```

# FizzBuzz

The goal here is to Write a program that prints numbers from 1 - 100 but for multiples of 3 print "Fizz" and for multiples of 5 print "Buzz". For multiples of 3 and 5 print "FizzBuzz

To start off we must define our starting number `num = 1`

```
while num <= 99:
    num = num+1
```
A while loop will run a piece of code while a condition is True. It will keep executing until that condition is no longer True.
Because `num` is set at 1, the while loop will allow for this repeated execution until it hits 99, but in reality it is 100 due to the nature of the code.

```commandline
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```
As seen in the odd and even exercise we once again use Modulo(`%`) to detect if the numbers are multiples of 3 or 5.

This will leave us with a printed list of numbers from 1 to 100, with numbers divisible by 3 shown as Fizz, and divisible by 5 known as Buzzz.