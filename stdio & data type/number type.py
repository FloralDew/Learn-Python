# 整数类型：不可变数据类型
DEC = 154546 # 不加引导符默认10进制
BIN = 0b1010111
OCT = 0o1234567
HEX = 0x98af56b
# 无论是引导符还是16进制中的字母，大小写均可
print(HEX) # 默认以10进制输出


# 浮点数类型：不可变数据类型
height=187.
print(height,'数据类型是',type(height)) # float

h=187
print(h,'数据类型是',type(h)) # int

sci = 5e1 # e后面的必须是整数
print(sci,'数据类型是',type(sci)) #float

# 浮点数计算精度误差问题
print(0.1 + 0.2) # 0.30000000000000004
print(round(0.1 + 0.2, 1)) # 保留1位小数 0.3 方法：四舍六入五成双


# 复数
c = 5+2j # 虚数单位是j而不是数学上的i
print('c的实数部分是',c.real,'类型是',type(c.real),'虚数部分是',c.imag,'类型是',type(c.real)) # float

# 何为不可变数据类型：元素改变地址改变
print(id(c))
c = 5-2j
print(id(c))