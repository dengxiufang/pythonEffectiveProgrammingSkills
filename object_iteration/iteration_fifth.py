# 如何在一个 for 语句中迭代多个可迭代对象


# 实际案例
# 1 某班学生期末考试成绩,语文，数学，英语
# 分别存储在3个列表中，同时迭代三个列表，计算每个学生的总分
# (并行)
# 解决方案：使用内置函数 zip，他能将多个可迭代对象合并，每次迭代返回一个元祖
from random import randint

chinese = [randint(60,100) for _ in range(40)]
math = [randint(60,100) for _ in range(40)]
english = [randint(60,100) for _ in range(40)]
# 这种方法可行，但是如果带有生成器就不可使用了
for i in range(len(math)):
    chinese[i]+math[i]+english[i]
# 正确方法 zip 例子,取对应位置的元素合并为一个tuple
print(list(zip([1,2,3,4],('a','b','c','d'))))
print(list(zip(chinese,math,english)))
total = []

for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)

print(total)

# 实际案例
# 2 某年级有4个班，某次考试每班英语成绩分别存储在4个列表中。
#  依次迭代每个列表，统计全学年成绩高于90分人数
# (串行)
# 解决方案: 使用标准库中的 itertools,chain,它能将多个可迭代对象连接

from itertools import chain

for x in chain([1,2,3,4],['a','b','c']):
    print(x)

e1 = [randint(60,100) for _ in range(40)]
e2 = [randint(60,100) for _ in range(42)]
e3 = [randint(60,100) for _ in range(42)]
e4 = [randint(60,100) for _ in range(39)]
count = 0

for s in chain(e1,e2,e3,e4):
    if s>90:
        count+=1
print(count)