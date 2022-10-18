# 通过类方法统计对像个数
# 通过类方法打印对象个数

class Wife:
    wife_num = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        Wife.wife_num += 1

    # 公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 21 <= age <= 40:
            self.__age = age
        else:
            raise ValueError("Age must be between 20 and 40")

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        if 50 <= weight <= 60:
            self.__weight = weight
        else:
            raise ValueError("weight must be between 50 and 60")

    age = property(get_age, set_age)
    weight = property(get_weight, set_weight)

    @classmethod
    def get_wife_num(cls):
        return cls.wife_num


wife01 = Wife("张三", 28, 50)
wife01.age = 30
print(wife01.age)
