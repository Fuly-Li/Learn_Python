# def sum(num1, num2):
#     # 两数之和
#     if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
#         raise TypeError('参数类型错误')
#     return num1 + num2
# print(sum(1, 99))
#
# def division(num1, num2):
#     # 求商与余数
#     a = num1 % num2
#     b = (num1 - a) / num2
#     return b, a
#
# num1, num2 = division(9, 4)
# tuple1 = division(9, 4)
#
# print(num1, num2)
# print(tuple1)


# def print_info(a, b=[]):
#     print(a,b)
#     return b;
#
# result = print_info(1)
# result.append('error')
# print_info(2)

print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))