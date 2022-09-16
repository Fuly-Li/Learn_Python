# 外层循环控制行
for i in range(3):
    # 内存循环控制列
    for j in range(4):
        print("*", end=" ")
    print("")

print("-------------------")

# 外层循环控制行
for i in range(4):
    # 内存循环控制列
    for j in range(6):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print("")
