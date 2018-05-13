# -*- coding: utf-8 -*-

# 如何读写 json 数据

# 实际案例，在python中如何读写json 数据

# 解决方案: 使用标准库中的 json 模块，其中 loads,dumps函数可以完成json 数据的处理


# python 对象转化为json 数据
import json

l = [  1,  2,'abc',{'name':'Bob','age':13}]

print(json.dumps(l)) # [1, 2, "abc", {"age": 13, "name": "Bob"}]

d = {'b':None,'a':4,'c':'abc'}

print(json.dumps(d)) #{"a": 4, "c": "abc", "b": null}

# 删除不必要的空格
print(json.dumps(l,separators=[',',':'])) #[1,2,"abc",{"age":13,"name":"Bob"}]

# 排序

print(json.dumps(d,sort_keys=True))  #{"a": 4, "b": null, "c": "abc"}

# 把 json 数据转化为 python 对象

print(json.loads('[1, 2, "abc", {"age": 13, "name": "Bob"}]'))


# 把python对象写入文件
with open('second_example/demo.json','wb') as f:
    json.dump(l,f)