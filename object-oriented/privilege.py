# 面向对象的三大特征：封装、继承、多态
# 封装：隐藏内部细节，对外提供操作方式

## 权限控制：通过对属性或方法添加下划线
# 双下划线开头：private，仅允许定义该属性或方法的类本身访问
# 单下划线开头：protected，仅供类本身和子类访问，但实际上外部代码也可以访问
# 首尾双下划线：特殊方法

class Student():
    # 首尾双下划线：特殊方法
    def __init__(self, name, age, gender):
        self._name = name # self._name是受保护的，仅供类本身和子类访问
        self.__age = age # self.__age是私有的，仅供类本身访问
        self.gender = gender # 普通的实例属性，类内部外部及子类都可以访问
    def _protectedFun(self):
        print('仅供类本身和子类访问')
    def __privateFun(self):
        print('仅供定义的类访问')
    def show(self): # 普通的实例方法
        self._protectedFun()
        self.__privateFun()
        print(self._name)
        print(self.__age)

# 类的外部
stu = Student('Mary', 20, 'F')
print(stu._name)
# print(stu.__age) # AttributeError: 'Student' object has no attribute '__age'
stu._protectedFun()
# stu.__privateFun() # AttributeError: 'Student' object has no attribute '__privateFun'

# 使用私有实例属性和实例方法
print(dir(stu)) # 查看对象的所有实例，发现私有实例（方法）实际上是前面加上了_类名
print(stu._Student__age)
stu._Student__privateFun()
# 但这种方式非常不推荐