class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    # __gender是私有的实例属性，不推荐在外部使用_Student__gender访问
    # 那如何在外部访问私有实例属性呢：定义同名（也可以不同名，习惯上同名）属性
    # 使用装饰器@property修饰方法，将方法转化为属性使用（只能查看不能修改，使用时不加括号）
    @property
    def gender1(self): # 习惯上就叫gender，此处为了演示
        return self.__gender
    # 如何使得属性可写 -> 设置修改器setter
    @gender1.setter # 必须和property中方法同名
    def gender1(self, value): # 必须和property中方法同名
        if value != 'M' and value != 'F':
            print('illegal! set to default: F')
            self.__gender = 'F'
        else:
            self.__gender = value
    
stu = Student("Mike", 'F')
print(stu.name, 'gender = ', stu.gender1)
stu.gender1 = 'M' # 若未设置setter，报错
print(stu.gender1)
