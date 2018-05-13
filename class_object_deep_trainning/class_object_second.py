# -*- coding: utf-8 -*-

# 如何为创建大量实例节省内存

# 某网络游戏中，定义了玩家类 Player(id,name,status,...)
# 每当一个在线玩家，在服务器程序内侧有一个 Player 的实例
# 当在线人数很多时，将产生大量实例(如百万级)
# 如何降低这些大量实例的内存开销


# 解决方案
# 定义类的 __slots__属性，它是用来声明实例属性名字的列表

class Player(object):
    def __init__(self, uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

class Player2(object):
    # 用来描述实例有那些属性
    # 关闭了动态添加,节省了内存
    __slots__ = ['uid','name','status','level']
    def __init__(self, uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


p1 = Player('0001','Jim')
p2 = Player2('0001','Jim')

print(set(dir(p1)) - set(dir(p2)))  # set(['__dict__', '__weakref__'])
# 后面两个占用了内存