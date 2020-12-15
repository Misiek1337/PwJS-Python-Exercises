#!/usr/bin/python3
import random as r

c, d = [], []

for i in range(8*8):
    c.append(r.randint(-10,10))
    d.append(r.randint(-10,10))

a = [c[x:x+8] for x in range(0, len(c), 8)]
b = [d[x:x+8] for x in range(0, len(d), 8)]

matrix_mult = [[0]*8 for x in range(8)] #initialize 2d matrix

for i in range(8):
    for j in range(8):
        for k in range(8):
            matrix_mult[i][j] += a[i][k] + b[k][j]

print("A: {}\nB: {} \nMULT: {}".format(a, b, matrix_mult))
