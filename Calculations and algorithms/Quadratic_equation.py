#!/usr/bin/python3
import math as m

print("Calculate roots of ax^2 + bx + c")
a, b, c = input("Enter a: "), input ("Enter b: "), input("Enter c: ")
a, b, c = float(a), float(b), float(c)

d = b**2 - 4*a*c

if d > 0:
    print ("x1 = {}, x2 = {}".format((-b + m.sqrt(d))/(2*a), (-b + m.sqrt(d))/(2*a)))

elif d == 0:
    print ("x = {}".format(-b/(2*a)))

elif d < 0:
    print ("No real solutions.")