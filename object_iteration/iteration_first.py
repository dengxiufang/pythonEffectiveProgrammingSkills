# 如何实现可迭代对象和迭代器对象
l = [1, 2, 3, 4]
s = 'abcde'

# 这个是可迭代对象,可迭代对象的条件是实现了 iter 方法
for i in l:
    print(i)
# 可迭代对象可以使用 iter 得到迭代器对象
print(iter(l))
# 生成迭代器对象 iterator
# 只有一个 next 接口
t = iter(s)
for i in t:
    print(i)

# 实战
# 描述 某软件要求，从网络抓取各个城市气温信息，并依次显示:
# 北京:15-20
# 天津:17-22
# 如果依次抓取所有的信息，那么会非常的浪费空间，我们希望
# 使用 "用时访问" 的策略,并且把所有城市气温封装到一个对象里，使用for 迭代

# 解决思路 Step1: 实现一个迭代器对象 WeatherIterator,next 方法每次返回一个城市气温
# Step2: 实现一个可迭代对象 WeatherIterable,__iter__方法返回一个迭代器对象

import requests


from collections import Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index +=1
        return self.getWeather(city)
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)

# 测试用例
for x in WeatherIterable([u'北京',u'上海',u'广州',u'长春']):
    print(x)