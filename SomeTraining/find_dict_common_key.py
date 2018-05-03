# 如何快速找到多个字典中的公共键(key)
# sample(序列a,n)
# 功能: 从序列 a 中随机抽取n个元素，并将n个元素以list形式返回

from random import randint,sample
# 从字符串中随机抽取四个字符，并以 list 形式返回
# print(sample("abcdefg",4))

s1 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}

s2 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}

s3 = {x:randint(1,4) for x in sample("abcdefg",randint(3,6))}

# keys() 以列表返回一个字典所有的键
s1.keys() #dict_keys(['f', 'a', 'b', 'e', 'd', 'g'])

# 取并集 轮数小还行，轮数大不行了
print(s1.keys() & s2.keys() & s3.keys())

# 另一种

map(dict.keys,[s1,s2,s3]) #[dict_keys[],dict_keys[],dict_keys[]]

from functools import reduce

# reduce() 函数会对参数序列中元素进行累积
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作
# ，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
data = reduce(lambda a,b:a & b,map(dict.keys,[s1,s2,s3]))
print(data)
