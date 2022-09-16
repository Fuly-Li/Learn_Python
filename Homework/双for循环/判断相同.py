list01 = [3, 80, 45, 80, 5, 45, 1, 1]

# 去重
list02 = []
for i in range(len(list01) - 1):
    for j in range(i + 1, len(list01)):
        if list01[i] == list01[j]:
            print("有一样的,一样的数为{}".format(list01[i]))
            list02.append(list01[i])

# 去重后，还剩的元素
list03 = []
for i in range(len(list01)):
    if list01[i] not in list02:
        list03.append(list01[i])
print(list03)
  