list = []
while True:
    num=str(input("请输入一个字符:"))
    if num =='':
        break
    else:
        list.append(num)

print(list)
resoult= ''.join(list)
print(resoult)