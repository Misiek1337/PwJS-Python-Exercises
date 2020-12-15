#!/usr/bin/python3
import os

directory = input("Enter the path of the directory: ") #Prints files from input directory, should work on both Windows and Linux OS

print ("Number of files in directory: {}".format(len(os.listdir(directory))))