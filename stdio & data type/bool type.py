
x = True # == 1
print(x,'类型是',type(x)) # bool
print(x + 10, '类型是', type(x + 10))

y = False # == 0
print(y + 1, '类型是', type(y + 1)) # bool和int运算过后变为int，即使是1

# Python中一切皆对象，皆有bool值，可以用bool()测试
print(bool(11)) # True
print(bool(0 + 0j)) # False
print(bool(1j)) # True
print(bool(0)) # False
print(bool(0.0)) # False
# -> 非0数布尔值皆为 True

print(bool('上海')) # True
print(bool('\0')) # True
print(bool(' ')) # True
print(bool('')) # False
# -> 非空字符串(含空白字符)的布尔值皆为 True

print(bool(True)) # True
print(bool(False)) # False
print(bool(None)) # False

'''
Induction:
布尔值为False:
1. False/None
2. 0, 0.0, 0j
3. 空序列(字符串、元组、列表、字典、集合)
4. 自定义对象的实例, __bool__()方法返回False或__len__()方法返回0
'''