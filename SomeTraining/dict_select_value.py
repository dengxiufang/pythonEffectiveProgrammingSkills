# 晒出字典中值高于90的项

from random import randint

d = {x: randint(60,100) for x in range(1,21)}

# 字典筛选式
finalD = {k:v for k,v in d.items() if v>90}

print(finalD)

