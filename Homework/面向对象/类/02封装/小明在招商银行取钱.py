# 小明在招商银行取钱

# 人类
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


# 银行类
class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property  # 银行名称
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property  # 银行的钱
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    # 取钱
    def draw_money(self, person, moeny):
        self.money -= moeny
        person.money += moeny

    # 存钱
    def save_money(self, person, moeny):
        self.money += moeny
        person.money -= moeny


xm = Person("小明", 0)
zsyh = Bank("招商银行", 10000)

zsyh.draw_money(xm, 5000)

print(xm.money)
