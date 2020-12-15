#!/usr/bin/python3
combination = 1337
key = 0
while combination != key:
    key = input("Enter key combination: ")
    if combination == int(key):
        print("Lock opened!")
    else:
        print("Wrong combination, enter the combination again")
