#!/usr/bin/python3
import math as m

class complex_number:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def out(self):
        if self.i < 0:
            return "{}{}i".format(self.r, self.i)
        else:
            return "{}+{}i".format(self.r, self.i)

    def abs(self):
        return m.sqrt(self.r ** 2 + self.i ** 2)

    def add(self, n):
        return complex_number(self.r + n.r, self.i + n.i)
    
    def sub(self, n):
        return complex_number(self.r - n.r, self.i - n.i)

    def mul(self, n):
        return complex_number(self.r * n.r - self.i * n.i, self.r * n.i + self.i * n.r)

if __name__ == '__main__':
    num1 = complex_number(1,2)
    num2 = complex_number(3,4)

    print("Addition: {} + {} = {}".format(num1.out(), num2.out(), num1.add(num2).out()))
    print("Subtraction: ({}) - ({}) = {}".format(num2.out(), num1.out(), num2.sub(num1).out()))
    print("Multiplication: ({}) * ({}) = {}".format(num1.out(), num2.out(), num1.mul(num2).out()))
    print("Absolute value of {}: {}".format(num2.out(), num2.abs()))