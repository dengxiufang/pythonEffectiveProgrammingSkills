
from random import randint


data = [randint(-10,10) for _ in range(10)]


s = set(data);

print({x for x in s if x%3 == 0})

