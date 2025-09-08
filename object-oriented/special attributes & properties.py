## 特殊方法__xxx__()
a = 10
b = 20
print(dir(a)) # Python中一切皆对象, 可以通过dir查看对象的方法和属性
print(a.__add__(b))
print(a.__sub__(b)) # subtract
print(a.__lt__(b)) # less than
print(a.__ge__(b)) # greater or equal
print(a.__ne__(b)) # not equal
print('-' * 50)
print(a.__mul__(b)) # multiply
print(a.__truediv__(b)) # 除法
print(a.__floordiv__(b)) # 整除
print(a.__pow__(2))

## 特殊属性__xxx___
class A:
    pass
class B:
    pass
class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = A()
b = B()
c = C('watashi', 19)

print('the property dict of a:', a.__dict__)
print('the property dict of b:', b.__dict__)
print('the property dict of c:', c.__dict__)

print('the class a belongs to:', a.__class__)
print('the class b belongs to:', b.__class__)
print('the class c belongs to:', c.__class__)

print('tuple of parent classes of A:', A.__bases__)
print('tuple of parent classes of B:', B.__bases__)
print('tuple of parent classes of C:', C.__bases__) # 爷爷类不显示

print('the first parent class of A:', A.__base__)
print('the first parent class of B:', B.__base__)
print('the first parent class of C:', C.__base__)
# 如果father A和father B有同名方法, 那么在调用时默认调用第一个父类的方法

print("A类的层次结构:", A.__mro__)
print("B类的层次结构:", B.__mro__)
print("C类的层次结构:", C.__mro__) # C类继承了A类, B类, 间接继承了object类

# 以下仍是特殊方法, 不是属性
print('A类的子类列表:', A.__subclasses__())
print('B类的子类列表:', B.__subclasses__())
print('C类的子类列表:', C.__subclasses__())