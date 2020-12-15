#!/usr/bin/python3
import os

directory = input("Enter the path of the directory: ")

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print("Renaming file {}".format(filename))
        os.rename("{}/{}".format(directory,filename),"{}/{}.png".format(directory,filename.removesuffix(".jpg")))