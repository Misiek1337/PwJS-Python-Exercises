#!/usr/bin/python3

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
product = 0

for i in range(4):
    product += a[i] * b[i]

print("Scalar product of vectors {} and {} is {}".format(a, b, product))
