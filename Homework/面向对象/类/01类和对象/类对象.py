# 通过类方法统计对像个数
# 通过类方法打印对象个数

class Wife:
    wife_num = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.set_age(age)
        self.__weight = weight
        Wife.wife_num += 1

    # 公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 21 <= age <= 40:
            self.__age = age
        else:
            raise ValueError("Age must be between 20 and 40")

    @classmethod
    def get_wife_num(cls):
        return cls.wife_num


wife01 = Wife("张三", 28, 50)
# wife02 = Wife("李四", 28, 60)
# wife03 = Wife("王五", 28, 55)

print(Wife.get_wife_num())
