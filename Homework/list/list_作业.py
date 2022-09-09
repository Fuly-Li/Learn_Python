# list = [54, 25, 12, 42, 35, 17]
#
# list_big = []
# i = 0
# for i in list:
#     if i > 30:
#         list_big.append(i)
# print(list_big)

# list_Demo = []
# for i in range(5):
#     num = (input("请输入数字:"))
#     list_Demo.append(num)
# print(max(list_Demo))

# 删除大于10的数
list01 = [9, 25, 12, 8]
i=0
for i in range(len(list01)-1,-1,-1):
    if list01[i]>10:
        list01.remove(list01[i])
print(list01)
 