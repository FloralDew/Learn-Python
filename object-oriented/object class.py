# 一个类如果没有继承任何类，默认继承object. 因此object是所有类的直接或间接父类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"name:{self.name}, age:{self.age}")

per = Person('Amy', 22)
print(dir(per))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', 
'__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', 
'__subclasshook__', '__weakref__', 'age', 'name', 'show']
'''
# 前面的一堆都是object类继承来的

# __init__()实际上是object类继承来的, 自己写的属于方法重写.
# 创建对象时先自动调用__new__(), 再在__init__()中赋值
# __str__()输出对象的描述信息, 在print(类对象)时被调用
## __str__方法重写:

class Person1(): # 不重写str方法
    def __init__(self, name):
        self.name = name

per1 = Person1("James")
print(per1) # 相当于print(per.__str__())

class Person2(): # 重写str方法
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This is a human.'

per2 = Person2("Alex")
print(per2)