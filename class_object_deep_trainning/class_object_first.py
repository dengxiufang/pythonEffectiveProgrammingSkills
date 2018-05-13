# -*- coding: utf-8 -*-

# 如何派生内置不可变类型并修改其改实例化行为

# 实际案例

# 我们想定义一种新类型的元组，对于传入的可迭代对象，
# 我们只保留其 int 类型且值大于 0 的元素，例如
# IntTuple([1,-1,'abc',6,['x','y'],3])=>(1,6,3)

# 要求 intTuple 是内置 tuple 的子类，如何实现

# 解决方案 定义类 inttuple 继承内置 tuple，并实现了 __new__,修改实例化行为
class IntTuple(tuple):

    def __new__(cls,iterable):
        g = (x for x in iterable if isinstance(x,int) and x>0)
        return super(IntTuple,cls).__new__(cls,g)
    def __init__(self,iterable):
        # before
        print(self)
        print(iterable)
        super(IntTuple, self).__init__(iterable)
        pass
        # after

t = IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)