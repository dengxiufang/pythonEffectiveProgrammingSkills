# 如何使用生成器函数实现可迭代对象

# 如下为生成器
def f():
    print('in f(),1')
    yield 1

    print('in f(),2')
    yield 2

    print('in f(),3')
    yield 3
# g 是生成器对象，也是可迭代对象
g = f()
for x in g:
    print(x)
# 其实 g 实现了 iter 方法，并且每次返回自身
print(g.__iter__() is g)


# 实际案例
# 实现一个可迭代对象的类，它能迭代出给定范围内所有素数

class PrimeNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end  = end

    def isPriimeNum(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k%i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.isPriimeNum(k):
                yield k

for x in PrimeNumbers(1,100):
    print(x)