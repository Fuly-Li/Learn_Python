# 敌人类：
# 数据：姓名:name，血量:blood，基础攻击力:atk，防御力:denfense
# 行为：打印个人信息

class Enemy:
    ATk = 0

    def __init__(self, name, blood, atk, defense):
        self.name = name
        self.blood = blood
        self.atk = atk
        self.defense = defense
        Enemy.ATk += atk

    # 行为
    def print_enemy_info(self):
        return self.name, self.blood, self.atk, self.defense

    # 该敌人是否在敌人列表中
    def find_enemy(self, name):
        if self.name == name:
            print("%s在敌人列表中，血量为：%d，攻击力为：%d，防御力为：%d" % (self.name, self.blood, self.atk, self.defense))
        else:
            print("%s该敌人不在敌人列表中" % self.name)


# 创建敌人列表
list01 = [Enemy("张三", 200, 80, 50), Enemy("灭霸", 1000, 1000, 1000), Enemy("李四", 0, 20, 5),
          Enemy("王五", 80, 50, 60)]


# 查找姓名是”灭霸“的敌人对象
def in_enemy(name):
    for i in list01:
        if i.name == name:
            print(i.name, i.blood, i.atk, i.defense)


in_enemy("灭霸")

# 查找所有死亡的的敌人
for i in list01:
    if i.blood <= 0:
        print("%s已死亡" % i.name)

# 计算所有敌人的平均攻击力
atp = Enemy.ATk / len(list01)
print("平均攻击力为%d" % atp)

# 删除防御力小于10的敌人
for i in list01:
    if i.defense < 10:
        list01.remove(i)
    print(i.print_enemy_info())

print("")
# 将所有敌人攻击力增加50
for i in list01:
    i.atk += 50
    print(i.print_enemy_info())
