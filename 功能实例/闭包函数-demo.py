#!/usr/bin/python
#-*-coding:utf-8 -*-

'''
   闭包函数的必要条件：
        1、闭包函数必须返回一个函数对象
        2、闭包函数返回的那个函数必须引用外部变量（一般不能是全局变量），而返回的那个函数内部不一定要return

'''

def line_conf(a, b):
    def line(x):
        return a * x + b
    return line


# 定义两条直线
line_A = line_conf(2, 1)  # y=2x+b
line_B = line_conf(3, 2)  # y=3x+2

# 打印x对应y的值
print(line_A(1))  # 3
print(line_B(1))  # 5


# NO.2
def line_conf():
    a = 1
    b = 2
    def line(x):
        print(a * x + b)
    return line


# NO.3
def _line_(a, b):
    def line_c(c):
        def line(x):
            return a * (x ** 2) + b * x + c
        return line
    return line_c
