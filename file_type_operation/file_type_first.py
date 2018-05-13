# -*- coding: utf-8 -*-
# 如何读写 csv 数据


# 实际案例
# http://table.finance.yahoo.com/table.csv?s=000001.sz
# 我们可以通过雅虎网站获取这个股市数据集，它以 csv 数据格式存储
# 这里以天气数据作为例子
# 在 2015 年中 最高起温高于 40 度的记录存储到另一个 csv 文件中

# 解决方案

# 使用标准库中的 csv 模块,可是使用其中 reader 和 writer 完成 csv 文件读写

from urllib import urlretrieve

# urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz','pingan.csv')

# 读
import csv
rf = open('first_example/sitka_weather_07-2014.csv','rb')

reader = csv.reader(rf)


# 写

wf = open('first_example/demo2.csv','wb')

writer = csv.writer(wf)

writer.writerow(reader.next())

wf.flush()


# 解决方案

import csv

with open('first_example/sitka_weather_07-2014.csv','rb') as rf:
    reader = csv.reader(rf)
    with open('first_example/demo2.csv','wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2015-01-01':
                continue;
            if int(row[1]) > 40:
                writer.writerow(row)


print('end')

