# 如何判断字符串a是否以字符串b开头或结尾

# 实际案例
# 某文件系统目录下有一系列文件:
# qucicksort.c
# graph.py
# heap.java
# install.sh
# stach.cpp
# 编写程序给其中所有.sh文件和.py文件加上用户可执行权限


# 解决方案
# 使用字符串 str.startswith()
# str.endswith()
# 注意: 多个匹配时参数使用元组

import os,stat

dir  = './second_example/'
list = [name for name in os.listdir(dir) if name.endswith(('.sh','.py'))]

for file in list:
    os.chmod(dir+file, os.stat(dir+file).st_mode | stat.S_IXUSR)

print(oct(os.stat('./second_example/e.py').st_mode))

print(stat.S_IXUSR)
