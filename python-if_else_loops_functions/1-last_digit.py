#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = abs(number) % 10
    last = int(-last)
else:
    last = int(str(number)[-1])
    last = int(last)

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")

if last == 0:
    print(f"Last digit of {number} is {last} and is 0")

if last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
