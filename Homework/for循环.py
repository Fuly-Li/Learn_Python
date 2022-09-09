# 求和
def sum(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    print(sum)


# 求偶数和
def sum2(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum += i
    print(sum)


# 求范围内和
def sum3(tou, wei):
    sum = 0
    for i in range(tou, wei + 1):
        sum += i
    print(sum)


sum(100)
sum2(100)
sum3(10, 36)
