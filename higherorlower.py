import random

correct_answer = random.randint(1, 20)
print("Guess a number between 1 and 20. You have 3 guesses")

num1 = int(input())

if num1 == correct_answer:
    print("You are correct!")
elif num1 > correct_answer:
    print("Your guess is too high. You have 2 guesses left.")
else:
    print("Your guess is too low. You have 2 guesses left.")

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

