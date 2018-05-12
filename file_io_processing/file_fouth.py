# -*- coding: utf-8 -*-

# 如何将文件映射到内存

# 实际案例

# 1. 在访问某些二进制文件时，希望能把文件映射到内存，可以随机访问.(framebuffrt 设备文件)

# 2. 某些嵌入式设备，寄存器被编址到内存地址空间，我们可以
# 映射 /dev/mem 某范围，去访问这些寄存器

# 3. 如果多个进程映射同一个文件，还能实现进程通信的目的


# 解决方案
# 使用标准库中 mmap 模块的 mmap()函数
# 它需要一个打开的文件描述作为参数
#
# 创建一个大小为 1M 每个字节都是 0 的二进制文件
# dd if=/dev/zero of=demo.bin bs=1024 count=1024
# 以 十六进制查看文件
# od -x demo.bin

import mmap
import os

f = open('fouth_example/demo.bin','r+b')
# f.fileno()  创建一个文件描述符号
# 第一个参数文件描述符号
# 第二个参数映射的文件长度 0表示整个文件
# 第三个参数 访问权限
# 第四个参数 跳过文件长度
m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)

m[0]='\x88'
m[4:8] = '\xff'* 4

m2 = mmap.mmap(f.fileno(),mmap.PAGESIZE*8,access=mmap.ACCESS_WRITE,offset=mmap.PAGESIZE*4)

m2[:0x1000] = '\xaa'* 0x1000