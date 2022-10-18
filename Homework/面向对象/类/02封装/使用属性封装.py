# 通过类方法统计对像个数
# 通过类方法打印对象个数
class Wife:
    wife_num = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        Wife.wife_num += 1

    @property  # 创建property对象，只负责拦截读取操作
    def age(self):
        return self.__age

    @age.setter  # 只负责拦截写入操作
    def age(self, age):
        if 21 <= age <= 40:
            self.__age = age
        else:
            raise ValueError("Age must be between 20 and 40")

    @property  # 创建property对象，只负责拦截读取操作
    def weight(self):
        return self.__weight

    @weight.setter  # 只负责拦截写入操作
    def weight(self, weight):
        if 50 <= weight <= 60:
            self.__weight = weight
        else:
            raise ValueError("weight must be between 50 and 60")

    @classmethod
    def get_wife_num(cls):
        return cls.wife_num


wife01 = Wife("张三", 28, 50)
wife01.age = 30
wife01.weight = 100
print(wife01.age)
print(wife01.weight)
