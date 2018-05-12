# 如何对字符串进行左，右，局中对齐

# 实际案例
# 某个字典存储了一些列属性之
# {
#     "lodDist":100.0,
#     "SmallCull":0.04,
#     "DsitCull": 500.0,
#     "trilinear":40,
#     "farclip":477
# }
# 在程序中我们想以下工整的格式将其内容输出,如何处理?
# SamllCull: 0.04
# farclip: 477
# lodDist: 100.0
# DistCull: 500.0
# trilinear: 40


# 解决方案
# 方法一: 使用字符串 str.ljust(),str.rjust(),str.center() 进行左，右，居中对齐

s  = 'abc'
a = s.ljust(20,'=')
b = s.rjust(20,'=')
c = s.center(20)
print(a)
print(b)
print(c)


d = {
    "lodDist":100.0,
    "SmallCull":0.04,
    "DsitCull": 500.0,
    "trilinear":40,
    "farclip":477
}

#print(list(map(len,d.keys())))

w = max(map(len,d.keys()))

for k in d:
    print(k.ljust(w),':',d[k])


# 方法二 使用 format()格式方法
# < 表示左对齐
# > 表示右对齐
# ^ 表示居中
format(s,'<20')