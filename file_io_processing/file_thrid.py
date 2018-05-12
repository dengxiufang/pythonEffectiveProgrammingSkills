# -*- coding: utf-8 -*-

# 如何设置文件的缓冲


# 将文件内容写入到硬件设备时，使用系统调用
# 这类 I/O 操作的时间很长
# 为了减少 I/O 操作的次数，文件通常使用缓冲区
# (有足够多的数据才进行系统调用)
# 文件的缓冲行为，分为全缓冲，行缓冲，无缓冲

# 如何设置 python 中文件对象的缓冲行为?

# 解决方案
# 全缓冲 open 函数的 buffering 设置为大于1的整数n,n为缓冲区大小

f = open('thrid_example/demo.txt','w',buffering=2048)
f.write('+'* 1024)
f.write('+'* 1023)
f.write('-'* 2)

# 行缓冲 open 函数的 buffering 设置为 1


f2 = open('thrid_example/demo2.txt','w',buffering=1)
f2.write('abcd')
f2.write('1234')
f2.write('\n')

# 无缓冲 open 函数的 buffering 设置为 0
f3 = open('thrid_example/demo3.txt','w',buffering=1)
f3.write('a')

#


