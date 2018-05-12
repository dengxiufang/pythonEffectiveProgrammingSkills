# -*- coding: utf-8 -*-

# 如何处理二进制文件

# 实际案例

# wav 是一种音频文件的格式，音频文件为二进制文件
# wav 文件由头部信息和音频采样数据构成，前 44 个
# 字节为头部信息，包括声道数，采样频率，PCM 位宽等等
# 后面是音频采样数据
# 使用 python，分析一个 wav 文件头部信息，处理音频数据



# 解决方案
# open 函数想以二进制模式打开文件，指定mode参数为 'b'
# 二进制数据可以用 readinto,读入提前分配好的buffer中，便于数据处理
# 解析二进制数据可以使用标准库中的 struct 模块的 unpack 方法

import struct

# 两位 使用 小端模式 存储 从低地址往高地址存储 \x => \xhh 两位十六进制数
# \x0201 512+1
# short 类型
res = struct.unpack('h','\x01\x02')
print(res)

# 使用 大端模式 存储 从高地址往低地址存储
# \x0102 256+2
res = struct.unpack('>h','\x01\x02')
print(res)




f = open('second_example/demo.wav','rb')

info = f.read(44)

channel = struct.unpack('h',info[22:24])
print(channel)
# 占四位字节
samplingFrequency = struct.unpack('i',info[24:28])
print(samplingFrequency)
#
codeWidth = struct.unpack('h',info[34:36])
print(codeWidth)

import array

# 获取文件总字节数
# 将指针已到文件末尾
f.seek(0,2)
# 报告文件指针位置
# f.tell() 文件大小
n = (f.tell()-44)/2
# 生成缓冲区
buf = array.array('h',(0 for _ in xrange(n)))

f.seek(44)

r = f.readinto(buf)

for i in xrange(n):
    buf[i]/=8

f2 = open('second_example/demo2.wav','wb')

f2.write(info)

buf.tofile(f2)

f2.close()