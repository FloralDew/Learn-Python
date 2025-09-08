# __init__()实际上是object类继承来的, 自己写的属于方法重写.
# 创建对象时先自动调用__new__(), 再在__init__()中赋值
# __str__()输出对象的描述信息, 在print(类对象)时被调用
## __str__方法重写:

class Person(): # 不重写str方法
    def __init__(self, name):
        self.name = name

per = Person("James")
print(per) # 相当于print(per.__str__())

class Person1(): # 重写str方法
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This is a human.'

per1 = Person1("James")
print(per1)