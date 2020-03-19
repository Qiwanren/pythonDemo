#!/usr/bin/python
#-*-coding:utf-8 -*-

class Person:
    def __init__(self,name,weight):
        self.name = name
        self.tz = weight

    def run(self):
        self.tz = self.tz - 0.7

    def eat(self):
        self.tz = self.tz + 1


p = Person("小明",75)
print(p.tz)

p.run()
print(p.tz)

p.eat()
print(p.tz)