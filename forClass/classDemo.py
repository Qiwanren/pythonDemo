#!/usr/bin/python
#-*-coding:utf-8 -*-

### 类和对象
'''
    主要内容
        1、了解什么是对象和类
        2、面向对象的3个主要特征：继承、封装和多态4


    类：拥有共同特征的同一类事物的总称或抽象
        特点：1、多继承
    对象：将抽象的事物具体化，从类创建对象也叫类的实例化

'''

### 创建一个类
class Person:

    ## 创建一个方法，self 对象为默认传入的对象，创建方法的同时，
    # 使用self.name创建了一个成员变量，并对其赋值
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

class Worker(Person):

    def work(self):
        print(self.name + " begin to work!")

#person = Person()  ### 类对象的实例化
#person.setName('qiwanren')
#print(person.getName())

work = Worker()
work.setName('qiwanren')
work.work()