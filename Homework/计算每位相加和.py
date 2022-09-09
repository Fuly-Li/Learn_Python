number = int(input('请输入一个整数:'))


def qiuhe(number):
    qian = int(number / 1000 % 10)
    bai = int(number / 100 % 10)
    shi = int(number / 10 % 10)
    ge = int(number % 10)
    return qian+bai+shi+ge

print(qiuhe(number))
