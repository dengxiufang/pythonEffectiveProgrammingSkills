# -*- coding: utf-8 -*-

# 如何拆分含有多种分隔符的字符串

# 实际案例:
# 我们要把某个字符依据分隔符号拆分不同的字段
# 该字符串包含多种不同的分隔符,例如:

# s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# 其中 ，; \t | 都是分隔符号，如何处理?

# 解决方案1
# 连续使用 str.split()方法，每次处理一种分隔符号

def mySplit(s,ds):
    res = [s]

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    return [x for x  in res if x]


s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
print(mySplit(s,';,|\t'))

# 方法二
# 使用正则表达式的 re.split()方法，一次性拆分字符串

import re
print(re.split('[,;\t|]+',s))


