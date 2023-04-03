# if, elif, and else

# age = 17
#
# if age >= 18:
#     print("You are the correct age to buy a ticket for this movie")
# elif age <= 17:
#     print("You are younger than 18")

film_rating = "Mohammad"

if film_rating.lower() == "universal":
    print("Any ages can watch")
elif film_rating.lower() == "pg":
    print("Parental Guidance")
elif film_rating.lower() == "12":
    print("You must be 12 years or older")
elif film_rating.lower() == "15":
    print("You must be 15 or older")
elif film_rating.lower() == "18":
    print("You must be 18 or older")
else:
    print("Error. Please try again!")

# THERE ARE NO SWITCH OR CASE STATEMENTS IN PYTHON