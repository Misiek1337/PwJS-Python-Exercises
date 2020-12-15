#!/usr/bin/python3
import random as r

a = []
size = r.randint(2,10)

for i in range(size**2):
    a.append(r.randint(-10,10))

a = [a[x:x+size] for x in range(0, len(a), size)]

#Recursive determinant function from linear algebra library

def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
     
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    for fc in indices:
        As = A 
        As = As[1:] 
        height = len(As) 
 
        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det

    return total

print("A: {} \nDET: {}".format(a, determinant_recursive(a)))

