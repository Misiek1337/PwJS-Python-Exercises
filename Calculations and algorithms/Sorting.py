#!/usr/bin/python3
import random as r

numbers = []
for i in range(50):
    numbers.append(r.random())

check = sorted(numbers, reverse=1)

for i in range(len(numbers)-1):
    for j in range (len(numbers)-i-1):
        if numbers[j] < numbers [j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)
print(check)
if numbers == check:
    print("Sorting OK!")