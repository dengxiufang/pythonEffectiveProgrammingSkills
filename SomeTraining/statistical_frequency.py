# 如何统计序列中元素的出现频度

# 某随机序列 [12,5,6,4,6,5,5,7,...]中
# 找到出现次数最高的3个元素，他们出现次数是多少

from random import randint
data = [randint(0,20) for _ in range(30)]
print(data)

# 第一种方法

# 使用 data 的值作为键,初始化 0 为值
c = dict.fromkeys(data,0)
#print(c)

for x in data:
    c[x]+=1
# 然后根据字典的值进行排序,在 dict_sort.py 中实现

print(c)
# 第二种方法
# 使用 collections.Counter 对象

from collections import Counter

# 得到键值
c2 = Counter(data)

print(c2.most_common(3))

# demo2 对英文文章的单词进行词频统计，找到出现次数最高的10个单词，它们出现次数是多少

import re
txt  = open('TrainingFile/codingStyle.txt').read();
c3 = Counter(re.split('\W+',txt))

print(c3.most_common(5))