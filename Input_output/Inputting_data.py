#!/usr/bin/python3
name, surname, date = input("Enter name, surname and date:").split() #separated by spaces
#name, surname, date = input("Enter name: "), input ("Enter surname: "), input("Enter date: ") #separated by line breaks
print("Name: {}\nSurname: {}\nBirth Date: {}".format(name,surname,date))