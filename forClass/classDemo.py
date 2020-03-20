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
    类的构造方法和初始化方法
        构造方法：
            1、构造方法 _new_ 在类实例化对象时第一个调用的方法，将返回实例对象
            2、始终都是类方法（即第一个参数为cls），必须返回一个类实例对象(cls)
            3、是在新式类中新出现的方法（而Python 3.x中默认都是新式类（也即object类默认是所有类的祖先），
                不必显式的继承object；Python 2.x中默认都是经典类，只有显式继承了object才是新式类）
            4、返回实例
                def __new__(cls, *args, **kwargs):
                    #func_suite
                    return object.__new__(cls, *args, **kwargs)
        初始化方法：
            一个初始化的方法，“self”代表由类产生出来的实例对象，” _ _ init _ _”将对这个对象进行相应的初始化操作
'''

### 创建一个类
class Person(object):

    ## 创建一个方法，self 对象为默认传入的对象，创建方法的同时，
    # 使用self.name创建了一个成员变量，并对其赋值
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

### 类的继承
class Worker(Person):
    ## 默认构造方法，最先执行
    def __new__(cls, *args, **kwargs):
        print('_new_ 方法···')
        obj = super(Worker, cls).__new__(cls, *args, **kwargs)
        return obj
    ##  默认初始化方法，在_new_方法之后执行
    def __init__(self):
        print('_init_ 方法···')

    def work(self):
        print(self.name + " begin to work!")

#person = Person()  ### 类对象的实例化
#person.setName('qiwanren')
#print(person.getName())

work = Worker()
work.setName('qiwanren')
work.work()