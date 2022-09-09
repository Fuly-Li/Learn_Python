list_core = []

while True:
    str_core = input("请输入成绩:")
    if str_core == '':
        break
    list_core.append(int(str_core))
print(str(min(list_core)))
print(str(max(list_core)))
print("平均分："+str(sum(list_core) / len(list_core)))
