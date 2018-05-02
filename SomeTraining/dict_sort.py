#  如何根据字典中值的大小，对字典中的项排序

from random import randint

d = {x: randint(60,100) for x in 'xyzabc'}

print(d.keys())
print(d.values())

# 第一种利用 zip 将字典数据转化元组
data = sorted(zip(d.values(),d.keys()))
print(list(data))

# 第二种 传递 sorted 函数的key参数
print(d.items())
# key 的函数表示使用元祖的第二项进行比较排序
print(sorted(d.items(),key=lambda x:x[1]))