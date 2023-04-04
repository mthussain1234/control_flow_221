print("Welcome to the cinema. Please enter your age: ")

customer_age = int(input())
# if customer_age.isdigit:
if customer_age < 1 or customer_age > 117:
    print("Invalid Age! Please enter your correct age!")
elif customer_age < 18:
    print("You can watch movies rated U, PG, 12, 15")
elif customer_age < 15:
    print("You can watch movies rated U, PG, 12")
elif customer_age < 12:
    print("You can watch movies rated U, PG")
else:
    print("You can watch all the available movies!")
# else:
#     print("Invalid Input! Please enter a valid age.")
