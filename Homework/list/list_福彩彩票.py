import random
# 随机生成6个蓝球
list_cp = []
a = 0
while a < 5:
    i = random.randint(1, 33)
    if i not in list_cp:
        list_cp.append(i)
        list_cp.sort()
        a += 1

# 随机生成1个红球
i = random.randint(1, 16)
list_cp.append(i)

print(list_cp)