# 多态可以在程序运行过程中动态决定调用哪个对象的方法，提高程序的可扩展性
# Python中的多态与java不同，不关心对象的数据类型，
# 也不关心类之间是否存在继承关系，只关心对象的方法
# 只要不同的类中有同名的方法，即可实现多态

class Person():
    def eat(self):
        print('rice')
    # 没有实例属性不需要初始化方法

class Cat():
    def eat(self):
        print('fish')

class Dog:
    def eat(self):
        print('bone')
# 这三个函数有一个同名方法eat
def func(obj): # obj是函数的形参，在定义处不知道它的数据类型
    obj.eat()

# 创建三个类的对象
per = Person()
cat = Cat()
dog = Dog()
# 只有在运行时才知道obj的数据类型
func(per) # Python中的多态不关心对象的数据类型，只关心对象是否有同名方法
func(cat)
func(dog)