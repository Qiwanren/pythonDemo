#!/usr/bin/python
#-*-coding:utf-8 -*-

class Anamal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s 开始吃东西 ·····" % self.name)
    def drink(self):
        print("%s 开始喝水 ·····" % self.name)
    def run(self):
        print("%s 正在跑步 ·····" % self.name)
    def sleep(self):
        print("%s 开始睡觉了 ·····" % self.name)

class dog(Anamal):
    def bark(self):
        print("%s 在叫唤 ······" % self.name)

wangcai = dog("wangcai")
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.bark()