class Student():
    def __init__(self, name, age, socre, sex):
        self.age = age
        self.name = name
        self.score = socre
        self.sex = sex

    def print_student_info(self):
        print("%s年龄是%d，成绩是%d，性别是%s" % (self.name, self.age, self.score, self.sex))


list01 = [Student("张三", 18, 99, "男"), Student("李四", 22, 150, "女"), Student("王五", 20, 100, "男"),
          Student("张大炮", 50, 60, "女")]


# 找人，看这个人在不在列表中
def find_person(name):
    for i in list01:
        if i.name == name:
            print("姓名是：%s，年龄是：%d" % (i.name, i.age))


# 按性别找人
def find_sex(sex):
    for i in list01:
        if i.sex == sex:
            print("姓名是：%s，年龄是：%d，性别是：%s" % (i.name, i.age, i.sex))


# 统计年龄>30的人的数量
def statistical_age(age):
    a = 0
    for i in list01:
        if i.age >= age:
            a += 1
    # return a
    print("一共%d个人的年龄大于%d岁"%(a,age))

# 将所有学生的成绩改为0
def set_socre():
    for i in list01:
        i.score = 0




find_person("张三")
print("  ")
find_sex("女")

statistical_age(10)

# set_socre()
# for i in list01:
#     print(i.name,i.score)