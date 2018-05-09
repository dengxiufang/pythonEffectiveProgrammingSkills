# 过滤列表中的负数

from random import randint
import timeit;
 # 这里 _ 表示丢弃变量,和 for i in range(5) 没有区别
 # 生成 -10 10 之间的10个数
 # 后面生成的数值会被前面的替换

data = [randint(-10,10) for _ in range(10)]

# 第一种过滤器
print(list(filter(lambda x: x>=0,data)));


#print([item for item in data]);

# 第二种 列表解析,会比过滤器更加快
print([x for x in data if x>=0])
