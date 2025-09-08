class FartherA:
    def __init__(self, name):
        self.name = name
    def showA(self):
        print('父类A中的方法')

class FartherB(): # 括号可省略，默认继承object类
    def __init__(self, age):
        self.age = age
    def showB(self):
        print('父类B中的方法')

# 多继承
class Child(FartherA, FartherB):
    def __init__(self, name, age, gender):
        FartherA.__init__(self, name) # 不能用super()，不知道是哪个父类
        FartherB.__init__(self, age) # 用类名.调用需要加self参数
        self.gender = gender

son = Child('Michael', 18, 'X') # 调用Child中的__init__()
# name调用父类A中初始化方法赋值，age调用父类B中初始化方法赋值，gender调用子类自己的初始化方法
son.showA() # 调用父类A中的showA方法
son.showB()