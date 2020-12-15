#!/usr/bin/python3
import threading as t
import random as r
import time

#solution based on https://rosettacode.org/wiki/Dining_philosophers
class philosopher(t.Thread):
 
    running = True
 
    def __init__(self, name, leftfork, rightfork):
        t.Thread.__init__(self)
        self.name = name
        self.leftfork= leftfork
        self.rightfork = rightfork
 
    def run(self):
        while(self.running):
            time.sleep(r.randint(3, 10))
            print("{} is hungry.".format(self.name))
            self.eat()
 
    def eat(self):
        fork1, fork2 = self.leftfork, self.rightfork
 
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print("{} can't have two forks and puts his fork down.".format(self.name))
            fork1, fork2 = fork2, fork1
        else:
            return
 
        self.eating()
        fork2.release()
        fork1.release()
 
    def eating(self):			
        print("{} starts eating.".format(self.name))
        time.sleep(r.randint(1, 10))
        print("{} finishes eating and waits to get hungry again.".format(self.name))
 
class philosopher_deadlock(t.Thread):
 
    running = True
 
    def __init__(self, name, leftfork, rightfork):
        t.Thread.__init__(self)
        self.name = name
        self.leftfork= leftfork
        self.rightfork = rightfork
 
    def run(self):
        while(self.running):
            time.sleep(r.randint(3, 10))
            print("{} is hungry.".format(self.name))
            self.eat()
 
    def eat(self):
        fork1, fork2 = self.leftfork, self.rightfork

        #philosophers will not try to return the forks if they don't get two
        while self.running:
            fork1.acquire(True)
            fork2.acquire(True)
        else:
            return

        self.eating()
        fork2.release()
        fork1.release()
 
    def eating(self):			
        print("{} starts eating.".format(self.name))
        time.sleep(r.randint(1, 10))
        print("{} finishes eating and waits to get hungry again.".format(self.name))

names = ["Pythagoras", "Plato", "Socrates", "Aristotle", "Epicurus"]

def diningphilosophers():
    forks = [t.Lock() for n in range(5)]
 
    philosophers= [philosopher(names[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
 
    philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(50)
    philosopher.running = False
    print ("Philosophers finished dining.\n")

def diningphilosophers_deadlock():
    print("#################################\nDining philosophers problem with deadlock")
    forks = [t.Lock() for n in range(5)]
 
    philosophers= [philosopher_deadlock(names[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
 
    philosopher_deadlock.running = True
    for p in philosophers: p.start()
    time.sleep(50)
    philosopher.running = False
    print ("Philosophers finished trying to dine.")

diningphilosophers()
diningphilosophers_deadlock()