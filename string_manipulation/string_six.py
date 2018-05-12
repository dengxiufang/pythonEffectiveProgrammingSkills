# 如何去掉字符串中不需要的字符

# 实际案例
# 1. 过滤掉用户输入前后多余的空白字符:
#   '  nick2008@gmail.com   '
# 2. 过滤某 windows 编辑文本中的 '\r':
# 'hello world\r\n'
# 3. 去掉文本中的 unicode 组合符号(音调):
# u`jiào jiào jiào

# 解决方案
# 1. 字符串 strip(),lstrip(),rstrip()防范去掉字符串两端字符

s = '   abc  123   '
# 去除前后空格
print(s.strip())
# 去除前空格
print(s.lstrip())
# 去除后空格
print(s.rstrip())

s = '----abc++++'
print(s.strip('-+'))

# 2. 删除单个固定位置的字符,可以使用切片+拼接的方式

s = 'abc:123'
print(s[:3]+s[4:])

# 3. 字符串的 replace() 方法或正则表达式 re.sub()删除任意位置字符

s = '\tabc\t123\txyz'

print(s.replace('\t',''))

import re
s = '\tabc\t123\txyz\ropq\r'

print(re.sub('[\t\r]','',s))

# 4. 字符串 translate()方法,可以同时删除多种不同字符

s = 'abc1232323xyz'

import string

# 得到 abcxyz 的映射表 xyzabc
print(s.translate(s.maketrans('abcxyz','xyzabc')))
# xyz1232323abc

# python2 实现
# s2 = 'abc\refg\n2342\t'
# s3 = s2.translate(None,'\r\n\t')
# print(s3) # abcefg2342

u = "u'jiào jiào jiào"

print(u)