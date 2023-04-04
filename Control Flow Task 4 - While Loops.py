# Take 10 integers from user and print average value once you have them all

repeat = range(10)

store_num = []

for i in repeat:
    new_num = int(input("Please enter an integer: "))
    store_num.append(new_num)

# sum() adds up all elements in list, len()
# returns the number of items in a list,
# and it is useful in this case to work out the average, len returns an integer
avg = sum(store_num) / len(store_num)
print(f"Your average is: {avg}")

#Write a while loop to print the following series: 10, 20, 30 ....300

n = 10

while n <= 300:
    print(n)
    n += 10