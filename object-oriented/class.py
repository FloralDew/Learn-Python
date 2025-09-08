'''
面向过程：C
事物比较简单，可以用线性思维解决
面向对象：Python/Java/C++
事物比较复杂，无法线性解决

二者并非相互独立
宏观上，面向对象：类
微观上每个对象内部仍然以面向过程方式解决问题
'''

# 类：由许多对象抽取出相似的属性和行为从而归纳出的类别
class Animal(): # 小括号可省略；首字母大写
    pass

# 类是图纸，对象是基于图纸的具体实例
cat = Animal() # 代码Animal()即可创建对象，赋值给cat。故cat是Animal类型的对象
print(type(cat)) # <class '__main__.Animal'>

## 类的组成
class Student:
    school = 'Fudan University' # 类属性。直接定义在类中，方法外的变量
    # 实例方法：定义在类中的函数，必须自带参数self
    # 初始化方法，相当于C++中的构造函数
    # init的第一个参数很重要，常用self表示。C++中，是this
    def __init__(self, name, age): # self和age是局部变量
        self.s_name = name # 实例属性：定义在__init__方法中，即使用self.调用的变量
        self.age = age # 实例属性名可以和局部变量相同
    def show(self): # 这里参数也可以不叫self
        print(f'My name is: {self.s_name}. I\'m {self.age} yrs old.')
    def func(): # 不允许不加参数self 此处是为了演示
       print("no params")

    # 静态方法
    @staticmethod # 修饰后面紧跟的一个函数
    def sm(): # 不自带参数
        print('在静态方法中不能调用实例属性，也不能调用实例方法')
        # print(self.age)
        # self.show()
    
    # 类方法
    @classmethod
    def cm(cls): # 必须带参数cls
        print('在类方法中不能调用实例属性，也不能调用实例方法')

# 创建类的对象
stu = Student('sxn', 20) # self是自带的参数，无需手动传入，自动帮传
# 实例属性：使用对象名称.调用
print(stu.s_name, stu.age)
# 类属性：直接使用类名.调用
print(Student.school)

# 实例方法：使用对象名.调用
stu.show() # self自动传入
# stu.func() # Student.func() takes 0 positional arguments but 1 was given
# 类方法：使用类.调用
Student.cm()
# 静态方法：使用类.调用
Student.sm()
Student.func()
# Student.show() # Student.show() missing 1 required positional argument: 'self'
# ------> 简言之，用对象名.调用方法会自动传入self作为第一个位置参数，用类.则不会(但用类.类方法会自动传入cls)

stu2 = Student('Marry', 10)
lst = [stu, stu2, Student('Saki', 18)]
for item in lst:
    item.show()

# 动态绑定属性和方法：独属于某对象
stu.gender = 'Female'
print(stu.gender)
# print(stu2.gender) # AttributeError: 'Student' object has no attribute 'gender'

def intro():
    print('这是普通的函数，被动态绑定为stu2对象的方法')
stu2.fun = intro # 不能加括号
stu2.fun() # 动态绑定没有默认传参