'''
张无忌 教 赵敏 九阳神功
赵敏 教 张无忌 化妆
'''


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # 教
    def teach(self, person, skill):
        print(self.name, "教", person, skill)

    # 学
    def learn(self, person, skill):
        print(self.name, "学", person, skill)


zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach("赵敏", "九阳神功")
