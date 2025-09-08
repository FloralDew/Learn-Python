# 继承可以实现代码的复用
class Person: # 不继承任何类，默认继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Hello, I'm {self.name}. I'm {self.age} yrs old.")

# 编写Student类继承Person类，拥有父类中所有公有成员和受保护成员
class Student(Person): # 此时Person为父类，Student为子类，括号不能省略
    def __init__(self, name, age, stuID):
        super().__init__(name, age) # 调用父类的初始化方法，为name和age赋值
                                    # 用super().父类方法 不用加self
                                    # 必须接受父类__init__()中除了self的两个参数
        self.stuID = stuID # 子类自己的实例属性
    ## show方法重写。必须和父类同名(show)
    def show(self):
        # 调用父类中的方法(也可以不调用)
        super().show() # 不能输出学号
        print(f'my stuID: {self.stuID}') # 子类独有的

# 一个父类可以有多个子类
class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


stu = Student('Mike', 20, 243007) # 前两个参会调用父类中的初始化方法赋值，第三个才是自己的初始化方法
stu.show() # 若没有重写show方法，则是父类Person中的show方法；此处是子类重写后的
doc = Doctor('Jeff', 32, 'E.N.T.')
doc.show() # 父类Person的show方法，不能输出department