# 类
class Wife:
    # 数据成员
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    # 行为成员
    def play(self):
        print(self.name + "玩")


# 创建对象
wife = Wife("张三", "女")

# 调用方法
wife.play()


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
 