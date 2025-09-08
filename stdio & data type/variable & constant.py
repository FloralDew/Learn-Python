lucky_number = 8 # 整型变量
my_name = 'sb' # 字符串类型变量

print('my_name的数据类型是',type(my_name),'内容是'+my_name) # type()不能和字符串用+连接
# type()中也可以是常量，如'Shanghai'

# Python可以动态修改变量类型，只需要赋不同类型的值
my_name = 233 # 整型变量
print('my_name的数据类型是',type(my_name),'内容是',my_name)

# 允许多个变量指向同一个值
a = b = 'Shanghai'
print('a的地址是',id(a),'\nb的地址是',id(b)) # 地址相同

# 定义常量
PI = 3.14