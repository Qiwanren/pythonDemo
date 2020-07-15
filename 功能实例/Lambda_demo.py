#!/usr/bin/python
#-*-coding:utf-8 -*-

'''
    lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体

    lambda的四种用法：
        1、将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数
            add=lambda x, y: x+y   使用add(1,2)调用
        2、将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换
           time.sleep=lambda x:None
           这样在后续调用time.sleep(3)将什么都不做
        3、将lambda函数作为其他函数的返回值，返回给调用者
        4、lambda函数作为参数传递给其他函数


'''

add=lambda x, y: x+y
print(add(1,2))