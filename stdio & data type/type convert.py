
# 隐式类型转换
x = 3
y = 10
z = y / x
print(z, type(z))
t = y / 2 # 能除尽也会转换成float
print(t, type(t))

# 显式类型转换
print(int(z)) # 不四舍五入，只保留整数部分
print(int(-3.9)) # -3
print(ord('b'), type(ord('b'))) # int 类型
print(float(10)) # 10.0
print(hex(10))

# str 转 数字
print(int('100'))
# print(int('100.0')) # 报错
print(float('100.0')) # 加不加.0都不会报错
print(float(0xa)) # 默认输出十进制，且对于非十进制数，不能是字符串，如"0xa"

# 转str
print('number: ' + str(10))

# 进制转换
print(bin(520)) # 内部必须是整数
print(hex(0o10))