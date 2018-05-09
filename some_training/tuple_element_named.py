# 如何为元祖中的每个元素命名,提高程序可读性
# 元祖的优势在与 存储占用小，操组速度快

# 第一种方式，定义一系列的数值

NAME,AGE,SEX,EMAIl = range(4)


student = ('Jim',16,'male','jim8721@gamil.com')


# name
print(student[NAME])


# 使用标准库中 collections.nametuple 替代内置 tuple
from collections import namedtuple

Student = namedtuple('Student',['name','age','sex','email'])

s = Student('Jim',16,'male','jim8721@gamil.com')

print(s)
print(s.name)
# 任何使用元组的地方都可以使用
print(isinstance(s,tuple))