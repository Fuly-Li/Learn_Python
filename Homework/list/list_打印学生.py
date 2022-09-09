list_student = []

while True:
    str_name = input("请输入学生姓名:")

    if str_name == "":
        break
    if str_name not in list_student:
        list_student.append(str_name)
    else:
        print("该名字已存在")
print(list_student)
for i in range(-1, -len(list_student) - 1, -1):
    print(list_student[i])
