list01 = [["00", "01", "02", "03"],
          ["10", "11", "12", "13"],
          ["20", "21", "22", "23"],
          ["30", "31", "32", "33"],
          ["40", "41", "42", "43"]]


class Vector2:
    """
    二维向量
    可以表示位置/方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 静态方法：表示左边方向
    @staticmethod
    def left():
        return Vector2(0, -1)

    # 静态方法：表示右边方向
    @staticmethod
    def right():
        return Vector2(0, 1)

    # 静态方法：表示上边方向
    @staticmethod
    def up():
        return Vector2(-1, 0)

    # 静态方法：表示下边方向
    @staticmethod
    def down():
        return Vector2(1, 0)





class DoubleListHelper():
    # 获取列表 Vector(1,2) 右边 3个的数据
    # target 列表；vect_pos 位置；vect_dir 方向；count 个数
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
        在二维列表中，获取指定位置、指定方向、指定个数的数据
        """
        list_resule = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            elements = target[vect_pos.x][vect_pos.y]
            list_resule.append(elements)
        return list_resule


re = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
print(re)

re = DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 4)
print(re)
























# 作用：位置+方向
# pos01 = Vector2(1, 2)
# l01 = Vector2.left()
# pos01.x += l01.x
# pos01.y += l01.y
#
# print(pos01.x, pos01.y)