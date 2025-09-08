g = 10 # 全局变量

# 函数的参数和函数内定义的变量是局部变量
def calc(a, b):
    s = a + b
    return s + g
# print(a)
# print(b)
# print(s) # 均会报错
print(g)
print(calc(10, 20))

# 局部变量优先级更高
def calc2(g, f):
    print(g + f)
calc2(1, 2)
def calc3():
    g = 100
    print(g)
calc3()
print(g) # 局部无法修改全局变量

def calc4(a, b):
    global s # 声明全局变量
    s = a + b # 这种方法声明的全局变量，声明和赋值必须分开
calc4(5, 6)
print(s)