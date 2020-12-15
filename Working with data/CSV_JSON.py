#!/usr/bin/python3
import csv

action = 0
columnnames = 0
writefields = []

directory = input("Please input the location of your CSV file: ")
while columnnames != "y" and columnnames != "n":
    columnnames = input("Does the first row describe column names? y/n: ")

def displaycsv():
    f = open(directory, "r")
    csvfile = list(csv.reader(f))
    if columnnames == "y":
        print("Fields: {}".format(", ".join(csvfile[0])))
        fields = csvfile[0]
        for line in csvfile[1:]:
            print(", ".join(line))
    else:
        fields = 0
        for line in csvfile:
            print(", ".join(line))
    return fields

while action != "e":
    fields = displaycsv()
    action = input("Choose what would you like to do with the file - (w)rite, (r)emove, (e)xit: ")
    deleteaction = 0

    if action == "w":
        if columnnames == "y":
            for field in fields:
                value = input("{}: ".format(field))
                writefields.append(value)
        else:
            f = open(directory, "r")
            csvfile = list(csv.reader(f))
            for num in enumerate(csvfile[0]):
                value = input("field {}: ".format(num[0]))
                writefields.append(value)

        with open(directory, "a+", newline = '') as f:
            csvfile = csv.writer(f)
            csvfile.writerow(writefields)

        writefields.clear()
    
    if action == "r":
        f = open(directory, "r")
        csvfile = list(csv.reader(f))
        while deleteaction != "w" and deleteaction != "i":
            deleteaction = input("Remove by (w)ord or (i)ndex?: ")

        if deleteaction == "w":
            delete = input("input word to delete: ")

            for num, values in enumerate(csvfile):
                    if delete in values:
                        csvfile.pop(num)

        if deleteaction == "i":
            for num, values in enumerate(csvfile):
                   print("{} {}".format(num, ", ".join(values)))
            delete = input("input index to delete: ")
            csvfile.pop(int(delete))

        with open(directory, "w+", newline = '') as f:
            csvwritefile = csv.writer(f)
            csvwritefile.writerows(csvfile)

        deleteaction = 0