
# 加减乘除。注意int/int会隐式转换成float
# 整除
x = 10 // 3
print(x, type(x)) # int
print(10 / 3, type(10 / 3)) # float
print(10 / 2, type(10 / 2)) # float
# 模 %
print(type(10 % 2)) # int
print(type(5 % 1.)) # float
print(type(5. % 1)) # float
print(-3 % 2) # 1
print(3 % -2) # -1
# 幂运算**
print(2 ** 0.5)
print(2 ** 4, type(2 ** 4)) # int
print(2 ** 4., type(2 ** 4.)) # 16.0 float

'''
优先级
**
* / // %
+ -
'''