#!/usr/bin/python3
import os

directory = input("Enter the path of the directory: ")

##Solution without recursion.
#for dirpath, dirnames, filenames in os.walk(directory):
#    print(dirpath)
#    for file in filenames:
#        print("\t{}".format(file))


#Solution with recursion for Windows and Linux systems.

def recursive_tree(directory, recursion = 1):
    for path in os.listdir(directory):
        print("{}└──────{}".format(recursion*"\t", path))
        try:
            recursion+=1
            recursive_tree("{}/{}".format(directory, path), recursion)
        except:
            recursion-=1
            continue
        recursion-=1
    
print(directory)
recursive_tree(directory)