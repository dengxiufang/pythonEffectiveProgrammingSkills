# -*- coding: utf-8 -*-

# 如何读写文本文件

# 实际案例
# 某文本文件编码格式已知(UTF-8,GBK,BIG5),
# 在 python2.x 和 python3.x 中分别如何读取文件?


# 解决方案

# python2.x => 写入文件前对 unicode 编码，读入文件后对二进制字符串解码
# python3.x => open 函数指定 't' 的文本模式,endcoding 指定编码格式
# str  ->  bytes
# unicode ->  str

# eg  python2 文件读写

# f = open('first_example/py2.txt','w')
# s = u'你好'
# f.write(s.encode('gbk'))
# f.close()

# f = open('first_example/py2.txt','r')
# t = f.read()
# d = t.decode('gbk')
# print(d)

# eg python3 文件读写

f = open('first_example/py3.txt','wt')

f.write('你好,我是这样的')
f.close()
# t 表示以文本方式打开，不写默认是 t
f = open('first_example/py3.txt','rt',encoding='utf8')

s = f.read()

print(s)
