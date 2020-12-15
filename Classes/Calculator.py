#!/usr/bin/python3
from Complex_numbers import complex_number
import re

eq = input("Please enter the equation in format a + bi +/-/* c + di: ")

numbers = re.findall(r'-?\s?\d+', eq)

for index, number in enumerate(numbers):
    if " " in number:
        numbers[index] = number.replace(" ", "")

a, b, c, d = numbers[0], numbers[1], numbers[2], numbers[3]

a = float(a)
b = float(b)
c = float(c)
d = float(d)

num1 = complex_number(a,b)
num2 = complex_number(c,d)

if "*" in eq:
    print("{} = {}".format(eq, num1.mul(num2).out()))

else: 
    print("{} = {}".format(eq, num1.add(num2).out()))