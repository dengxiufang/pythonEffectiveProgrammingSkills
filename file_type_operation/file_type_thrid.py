# -*- coding: utf-8 -*-
# 如何解析简单的 xml 文档


# 使用标准库中的 xml.etree.ElementTree,其中的 parse函数可以解析xml数据

from xml.etree.ElementTree import parse

f = open('thrid_example/demo.xml')

et = parse(f)

root = et.getroot()

print(root.tag)
print(root.attrib)
print(root.text)

for child in root:
    print(child.get('name'))

# 查找 country 下所有节点
print(root.findall('country/*'))

# 查找 rank 节点
print(root.findall('.//rank'))

# 查找 rank 父节点
print(root.findall('.//rank/..'))

# 找到所有 country 节点
print(root.findall('country'))

print(root.findall('country[1]'))


# 找到名为 Singapore 的 country 节点

print(root.findall('country[@name="Singapore"]'))

