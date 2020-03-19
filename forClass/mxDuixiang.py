#!/usr/bin/python
#-*-coding:utf-8 -*-

## 定义类
class Cat:
    def __init__(self):
        ### 设置name属性
        self.name = "tom"
    def eat(self):
        # 哪一个对象调用的方法，self就是哪个对象的引用
        print("%s 爱吃鱼········" % self.name)
    def drink(self):
        print("%s 爱喝水········" % self.name)

### 创建对象
tom = Cat()

###  添加属性
#tom.name = "Tom"
tom.eat()
tom.drink()



