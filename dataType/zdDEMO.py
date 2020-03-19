#!/usr/bin/python
#-*-coding:utf-8 -*-

student = {"name":"小明",
           "age":28,
           "sex":"男"}

###  取值
print(student["name"])

### 增加，修改
student["age"] = 18
print(student["age"])

print(student)
###  删除
student.pop("name")
print(student)



