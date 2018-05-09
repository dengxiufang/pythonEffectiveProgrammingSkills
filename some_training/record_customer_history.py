# 如何实现用户的历史记录功能
# 以 python 2。7 运行
# 记录用户最后输入的五个数据
# 使用容量为 n 的队列存储历史记录
# 使用标准库 collections 中的deque，是一个双端循环队列
# 程序退出钱，可以使用 pickle 将对象存入文件，再次运行程序时将其导入

from collections import deque
from random import randint
import pickle

N = randint(0,100);


q2 = pickle.load(open('TrainingFile/history'))

if(q2):
    history = q2
else:
    history = deque([], 5)

def guess(k):
    if k == N:
        print("right");
    if k < N:
        print("%s is less-than N"%k)
    else:
        print("%s is greater-than N"%k)

while True:
    line = raw_input("please input a number:");
    print line
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line =="h?":
        print(list(history))
        pickle.dump(history, open('TrainingFile/history', 'w'));

