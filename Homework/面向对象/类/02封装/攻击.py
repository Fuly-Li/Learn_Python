class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def attack(self, other):
        # 攻击逻辑
        print("攻击了敌人")
        other.damage(self.atk)

    def damage(self, value):
        # 受伤逻辑
        print("玩家受伤了")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死了")
        print("屏幕碎了")


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        # 受伤逻辑
        self.hp -= value
        print("敌人受伤了")
        if self.hp <= 0:
            self.__death()

    def attack(self, other):
        print("敌人攻击玩家")
        other.damage(self.atk)

    # 私有的死亡方法
    def __death(self):
        # 死亡逻辑
        print("死亡")
        print("掉装备")
        print("加分")


p01 = Player(1000, 100)
e01 = Enemy(200, 50)

p01.attack(e01)
e01.attack(p01)
print('')
p01.attack(e01)
