'''
学生管理系统：
    1.完成数据模型类
    2.创建逻辑控制类
    3.完成数据：学生列表 __stu_list
    4.行为：获取列表 stu_list,
    5.添加学生方法 add_student
'''


class StudentModel:
    '''
    学生信息模型
    '''

    def __init__(self, name='', age=0, score=0, id=0):
        '''
        创建学生对象
        :param id: 编号（唯一标识）
        :param name: 姓名
        :param age: 年龄
        :param score: 分数
        '''
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


class StudentManagerController:
    '''
    学生管理控制器，负责业务逻辑处理
    '''
    # 学生初始ID
    __init_id = 1000

    def __init__(self):
        '''
        学生列表
        '''
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    # 自增学生ID
    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    # 添加学生
    def add_stu(self, stu_info):
        stu_info.id = self.__generate_id()
        self.stu_list.append(stu_info)

    # 根据ID删除学生
    def remove_stu(self, id):
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True  # 移除成功
        return False  # 移除失败

    # 根据ID修改其他信息
    def update_stu(self, stu_info):
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    # 按照成绩升序显示学生
    def sort_stu(self, stu_list):
        for i in range(len(stu_list) - 1):
            for j in range(i + 1, len(stu_list)):
                if stu_list[i].score > stu_list[j].score:
                    stu_list[i], stu_list[j] = stu_list[j], stu_list[i]


class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1.添加学生")
        print("2.显示学生")
        print("3.修改学生")
        print("4.删除学生")
        print("5.按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == '1':
            self.__input_students()
        elif item == '2':
            self.__output_students(self.__manager.stu_list)
        elif item == '3':
            self.__update_students()
        elif item == '4':
            self.__delete_students()
        elif item == '5':
            self.__sort_student(self.__manager.stu_list)
        else:
            print("请输入正确的数字")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    # 输入学生信息
    def __input_students(self):
        name = input("请输入学生姓名:")
        age = input("请输入学生年龄:")
        score = input("请输入学生成绩:")
        stu = StudentModel(name, int(age), int(score))
        self.__manager.add_stu(stu)
        print("***************************")

    # 输出学生信息
    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)
        print("***************************")

    # 删除学生信息
    def __delete_students(self):
        id = int(input("请输入需要删除的学生ID:"))
        if self.__manager.remove_stu(id):
            print("移除成功")
        else:
            print("移除失败")
        print("***************************")

    # 修改学生信息
    def __update_students(self):
        stu = StudentModel()
        stu.id = int(input("请输入需要修改信息的学生ID:"))
        stu.name = input("请输入新的学生姓名:")
        stu.age = int(input("请输入新的学生年龄:"))
        stu.score = int(input("请输入新的学生成绩:"))
        if self.__manager.update_stu(stu):
            print("修改成功")
        else:
            print("修改失败")
        print("***************************")

    # 按照成绩升序显示学生
    def __sort_student(self, list_output=None):
        self.__manager.sort_stu(list_output)
        for item in list_output:
            print(item.id, item.name, item.age, item.score)
        print("***************************")


view = StudentManagerView()
view.main()
