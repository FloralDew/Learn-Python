# Python中的有序组合数据类型：列表和元组
# Python中的无序组合数据类型：字典和集合

# 前面学过正向递增索引和反向递减索引

# 字符串只是序列中的一种
str = 'helloworld' # len = 10
for i in range (0, len(str)):
    print(i, str[i], end = " ")

print('\n')

for i in range (-10, 0): # 反向递减最后一个是-1
    print(i, str[i], end = " ")

print('\n')

# 序列的切片操作：[start = 0 : end(not included) = len : path = 1]
print(str[0:5:2]) # 0, 2, 4
print(str[0::2]) # 0, 2, 4, 6, 8
print(str[::2]) # 与上一行相同
print(str[5::])
print(str[5:]) # 与上一行相同
print(str[::-1]) # 逆序输出
print(str[-1:-11:-1]) # 与上一行相同 end不能是-10，因为不包含
# 切片直接返回原序列类型，可以直接赋值, 如a = str[::2], a还是字符串

# 序列的其他操作：相加、数乘
print('-' * 40)

print('world' in str) # in返回bool类型
print('hello' not in str) # not in返回bool类型
print(len(str)) # 求序列元素个数
print(max(str), type(max(str)), min(str)) # 求序列最大最小元素(ASCII) str

# 序列对象的方法：用.调用的叫方法
print(str.index('o'), type(str.index('o'))) # o第一次出现的位置 int
# print(str.index('v')) # ValueError: substring not found
print(str.count('o')) # 统计出现次数