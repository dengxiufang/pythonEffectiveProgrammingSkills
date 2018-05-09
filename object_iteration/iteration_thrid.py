# 如何进行反向迭代以及如何实现

l = [1,2,3,4,5]

# 反向的迭代器
#print(reversed(l))
# 正向的迭代器
#print(iter(l))

for x in reversed(l):
    print(x)

# 实际案例
# 实现一个连续浮点数发生器 FloatRange
# 根据给定范围(start,end)和步进值(step)产生一些连续浮点数
# 如迭代 FloatRange(3.0,4.0,0.2)可产生序列:

# 正向: 3.0->3.2->3.4->3.6->3.8->4.0
# 反向: 4.0->3.8->3.6->3.4->3.2->3,0

# 解决方案: 实现反向迭代协议的 __reversed__方法,它返回一个反向迭代器

class FloatRange:
    def __init__(self,start,end,step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t<self.end:
            yield t
            t += self.step
    def __reversed__(self):
        t = self.end
        while t >=self.start:
            yield t
            t -= self.step

for x in FloatRange(1.0,4.0,0.5):
    print(x)

for x in reversed(FloatRange(1.0,4.0,0.5)):
    print(x)
