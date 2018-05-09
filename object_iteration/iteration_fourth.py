
# 如何对迭代器进行切片操作

# 回顾一下如何进行文本读取

f = open('/var/log/daily.out')

#f[100:300]
# 可以使用如下方法进行读取，但是有个问题
# readlines 会将文件整个读进内存中，那么如果多大，会导致程序崩溃
# lines = f.readlines()
# print(lines[100:300])

# 最好的方式还是使用迭代器访问
# f.seek(0)
# for line in f:
#     print(line)

# 实际案例
# 有某个文本文件,我们想读取其中某范围的内容
# 如 100-300 行之间的内容，python中文本文件
# 是可迭代对象,我们是否可以使用类似列表切片
# 的方式得到一个 100～300行文件内容的生成器
#f = open('/var/log/daily.out')
#f[100:300] 可以吗?

# 解决方案: 使用标准库中的 itertools.islice,它能返回一个迭代对象切片的生成器

from itertools import islice
for line in islice(f,100,300):
    print(line,)

# 前 500 行
islice(f,500)
# 100到最后
islice(f,100,None)

# 对迭代器切片

l = range(20)

t = iter(l)
# 其实 0-4 也迭代了，这是抛弃了，islice 会消耗迭代器对象
for x in islice(t,5,10):
    print(x)
# 已经从 10 开始了
for x in t:
    print(x)