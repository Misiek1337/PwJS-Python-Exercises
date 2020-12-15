#!/usr/bin/python3
import random as r

c, d = [], []

for i in range(128*128):
    c.append(r.randint(-100,100))
    d.append(r.randint(-100,100))

a = [c[x:x+128] for x in range(0, len(c), 128)]
b = [d[x:x+128] for x in range(0, len(d), 128)]

matrix_sum = []

for i in range(128):
    for j in range(128):
        matrix_sum.append(a[i][j] + b[i][j])

matrix_sum = [matrix_sum[x:x+128] for x in range(0, len(matrix_sum), 128)]

index = input("Enter matrix index to check: ")
print("A[{}]: {}\nB[{}]: {} \nSUM[{}]: {}".format(index, a[int(index)], index, b[int(index)], index, matrix_sum[int(index)]))
