#通过类方法统计对像个数
#通过类方法打印对象个数

class Wife:
    wife_num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Wife.wife_num += 1

    @classmethod
    def get_wife_num(cls):
        return cls.wife_num


wife01 = Wife("张三", 18)
wife02 = Wife("李四", 28)
wife03 = Wife("王五", 28)

print(Wife.get_wife_num())
