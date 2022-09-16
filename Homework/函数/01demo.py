"""
计算四位数字，每位相加和
"""


def sum_number(num):
    result = num % 10
    result += num // 10 % 10
    result += num // 100 % 10
    result += num // 1000 % 10
    return result


print(sum_number(1236))
print()
