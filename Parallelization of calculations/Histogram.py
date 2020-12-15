#!/usr/bin/python3
import threading as t
import random as r

histogram= [0] * 5
num = 5

def calculate_histogram(lock, data):
    lock.acquire()

    for i in range(len(data)):
        if data[i] == 1:
            histogram[0] += 1
        if data[i] == 2:
            histogram[1] += 1
        if data[i] == 3:
            histogram[2] += 1
        if data[i] == 4:
            histogram[3] += 1
        if data[i] == 5:
            histogram[4] += 1
        
    lock.release()

def print_histogram(histogram): #3 7 3 2 5
    for i in range(max(histogram),0,-1):
        for j in range(len(histogram)):
            if histogram[j] >= i:
                print("#",end=" ")
            else:
                print(" ",end=" ")
        print("")


randomdata = []

for i in range(20):
    randomdata.append(r.randint(1,5))

lock = t.Lock()

for i in range(num):
    thread = t.Thread(target=calculate_histogram, args=(lock, randomdata))
    thread.start()
    thread.join()

for i in range(len(histogram)):
    histogram[i] = int(histogram[i]/num)

print_histogram(histogram)

print("Histogram of resulting list: {}".format(histogram))
