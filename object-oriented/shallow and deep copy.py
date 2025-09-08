# 变量的赋值: 只是形成两个变量, 实际指的还是同一个对象
# 类的浅拷贝: 拷贝时, 产生新对象, 但对象包含的子对象内容不拷贝. 源对象与拷贝对象会引用同一个子对象
# 类的深拷贝: 递归拷贝对象中包含的子对象. 源对象和拷贝对象所有的子对象也不相同

class A:
    pass
class B:
    pass
class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = A()
b = B()
c = C(a, b)

# 赋值
c_assign = c
print('c', 'id:', c, 'id of subobject:', c.a, c.b)
print('c_assign', 'id:', c_assign, 'id of subobject:', c_assign.a, c_assign.b) # 地址和c1相同
# 浅拷贝
import copy as cp
c_shallowcopy = cp.copy(c)
print('c_shallowcopy', 'id:', c_shallowcopy, 'id of subobject:', c_shallowcopy.a, c_shallowcopy.b) # 地址和c1相同
# 深拷贝
c_deepcopy = cp.deepcopy(c)
print('c_deepcopy', 'id:', c_deepcopy, 'id of subobject:', c_deepcopy.a, c_deepcopy.b) # 地址和c1相同