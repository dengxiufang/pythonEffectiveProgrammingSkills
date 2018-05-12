# -*- coding: utf-8 -*-

# 如何访问文件的状态

# 实际案例
# 我们需要获得文件状态
# 1. 文件的类型(普通文件，目录，符号链接，设备文件。。。)
# 2. 文件的访问权限
# 3. 文件的最后的访问/修改/节点状态更改时间
# 4. 普通文件的大小

# 解决方案
# 1.系统调用  标准库 os 模块下的三个系统调用 stat,fstat,lstat 获取文件状态
# 2.快捷函数 标准库中 os.path 下一些函数，使用起来更加简洁


# 可以取得链接文件的状态，不会继续跟踪 os.lstat()


# 方案 1
import os

s = os.stat('fifth_example/a.txt')
# 文件的类型,权限
bin(s.st_mode)  #0b1000000110100100

# stat 内置了非常多获取文件信息的内置方法
import stat

# 解决 1
# 是否是目录
stat.S_ISDIR(s.st_mode) # False
# 是否是普通文件
stat.S_ISREG(s.st_mode) # True

# 解决 2
# 是否可读,返回真值表示可读
s.st_mode & stat.S_IRUSR # 256
# 是否可写
s.st_mode & stat.S_IXUSR # 256

# 解决3
# 修改时间
s.st_atime  #1526143796.93
import time
# 转化时间
print(time.localtime(s.st_atime)) #time.struct_time(tm_year=2018, tm_mon=5, tm_mday=13, tm_hour=0, tm_min=49, tm_sec=56, tm_wday=6, tm_yday=133, tm_isdst=0)


# 解决4
# 文件大小

print(s.st_size)


# 方案 2

os.path.isdir('fifth_example/x.txt') # False

os.path.islink('fifth_example/x.txt') # True

os.path.isfile('fifth_example/x.txt') # True

print(os.path.getatime('fifth_example/a.txt'))
print(os.path.getsize('fifth_example/a.txt'))