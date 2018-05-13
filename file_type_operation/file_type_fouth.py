# -*- coding: utf-8 -*-
# 如何构建简单的 xml 文档


# 使用标准库中的 xml.etree.ElementTree,其中的 write函数可以写入文件

# 这里以天气的 csv 文件转化为 xml 为例

from xml.etree.ElementTree import Element,ElementTree,tostring


# 创建元素
e = Element('Data')
# 设置名称
e.set('name','abc')
print(tostring(e))  #<Data name="abc" />

# 设置内容
e.text = '123'
print(tostring(e))  #<Data name="abc" />123</Data>

# 添加自元素

e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'

e2.append(e3)

print(tostring(e2))  #<Row><Open>8.80</Open></Row>


e.text=None
e.append(e2)

print(tostring(e))  #<Data name="abc"><Row><Open>8.80</Open></Row></Data>


et = ElementTree(e)
et.write('fouth_example/demo.xml')


# 完成案例
import csv

def pretty(e,level=0):
    if len(e)>0:
        e.text = '\n'+'\t'*(level+1)
        for child in e:
            pretty(child,level+1)
        child.tail = child.tail[:-1]
    e.tail = '\n'+'\t'*level

def csvToxml(fname):
    with open(fname,'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag,text in zip(headers,row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    pretty(root)
    return ElementTree(root)
et = csvToxml('first_example/sitka_weather_07-2014.csv')

et.write('fouth_example/sitka_weather_07-2014.xml')

