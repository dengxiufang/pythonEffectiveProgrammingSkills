# 如何让字典保持有序

d = {}
d['Jim']=(1,35)
d['Leo']=(2,37)
d['Bob']=(3,40)

# python3 虽然会记录插入顺序，但是不建议使用

# for k in d: print(k)
# output:
# Jim
# Leo
# Bob

# 使用 OrderDict
from collections import OrderedDict

b = OrderedDict();
b['Jim']=(1,35)
b['Leo']=(2,37)
b['Bob']=(3,40)
for k in b: print(k)


# 按排名顺序依次打印选手成绩

from time import time
from random import randint
from collections import OrderedDict

score = OrderedDict()
# 生成八位选手
player = list('ABCDEFGH')
# 设置开始时间
start = time()

# range(8) [1,2,3,4,5,6,7] 不包含最后一个值
for i in range(8):
    # 输入回车表示一位选手答题结束
    input()
    # 随机选取一位选手模拟
    p = player.pop(randint(0,7-i))
    # 记录答题时间
    end = time()
    print(i+1,p,end-start)
    # 记录该选手答题名次和所用时间
    score[p] = (i+1,end-start)
print()
print("_"* 20)
for k in score:
    print(k,score[k])