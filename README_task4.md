# Take 10 integers from user and print average value once you have them all

`repeat = range(10)`

`store_num = []`

```for i in repeat:
    new_num = int(input("Please enter an integer: "))
    store_num.append(new_num)
 ```
`sum()` adds up all elements in list, `len()` returns the number of items in a list, and it is useful in this case to work out the average.

`avg = sum(store_num) / len(store_num)`

`print(f"Your average is: {avg}")`

Output is as follows:
```commandline
Please enter an integer: 3
Please enter an integer: 1
Please enter an integer: 2
Please enter an integer: 4
Please enter an integer: 6
Please enter an integer: 2
Please enter an integer: 3
Please enter an integer: 4
Please enter an integer: 5
Please enter an integer: 8
Your average is: 3.8
```

# Write a while loop to print the following series: 10, 20, 30 ....300

`n` will have an initial value of 10
The `while` loop will keep happening as long as `n` is less than or equal to 300
The `+=` allows the `n` value to be updated for the next loop, still following the sequence.
```
n = 10

while n <= 300:
    print(n)
    n += 10
   ```

Output is as follows:

```commandline
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300

Process finished with exit code 0

```