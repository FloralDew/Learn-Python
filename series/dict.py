# 字典是可变数据类型，无序：第一个添加到字典中的元素在内存中不一定在第一位
# 字典的键必须是不可变序列，比如str/int/float/tuple，不可重复；值可以重复

## 字典的创建

# (1){key:value,...}
d = {1:'A', 2:'B', 3:'C', 2:'D'} # 拥有两个相同的键
print(d) # 不会报错，但会导致后面的D覆盖掉B
# 字典中的元素应当是无序的，输出有序是因为Python3.6后解释器对其进行了处理

# (2)zip
lst1 = [1, 2, 3, 4]
lst2 = list("ABCDE") # value比key多一个
zipobj = zip(lst1, lst2)
print(zipobj) # zip object类型
print(list(zipobj)) # 列表类型，元素是元组
print(dict(zipobj)) # 此时zipobj已经没东西了，输出空字典{}

print(dict(zip(lst1, lst2))) # 这样就是字典，最后多出的E被舍去
print(dict(zip(tuple(range(10)),tuple("ABCDEF")))) # zip也可以输入tuple, set。后面多出的key也会被舍去
# 但要注意set是无序的，使用zip会导致键值对随机匹配

# (3)使用参数
d = dict(cat = 10, dog = 20) # key = value. cat和dog在外不可见
print(d)
print(type(tuple(d.keys())[0])) # <class 'str'> 键为str类型 'cat'
# 元组为键
e = {(1, 2): 3}
print(e)
# d = {[1, 2]: 3} # 报错，列表没有哈希

print(max(d)) # 求key的最大值
print(len(d)) # 求元素个数(键值对)

## 字典生成式
import random
e = {key:random.randint(1, 100) for key in range(1, 11)}
print(e)
e = {key:value for key,value in zip(lst1, lst2)}
print(e)

## 字典的删除
del e
# print(e) # name 'e' is not defined

## 字典元素的访问和遍历
d = {'hello':10, 'world':20, 'python':30}
print(d['hello']) # []中是索引
print(d.get('java', False)) # False缺省为None
# 区别：如果键不存在，上一种会报错，而下一种可以指定缺省值

for item in d.items(): # item是键值对，以元组形式呈现
    print(item)

for key, value in d.items():
    print(key, '->', value)

for key in d.keys():
    print(key, '-->', d[key])

## 向字典中添加元素
d['java'] = 40
print(d)

## 字典常用函数
# 获取字典所有key
keys = d.keys()
print(keys, type(keys)) # <class 'dict_keys'>
print(list(keys)) # 可以转化为列表、元组
print(tuple(keys))

# d.values() 同理

# 将字典中的数据转换为以键值对元组为元素的列表
lst = list(d.items())
print(lst)
print(dict(lst)) # 反向转换
# 元素为列表也可以
print(dict([['hello', 10], ['world', 20], ['python', 30], ['java', 40]]))

# pop
a = d.pop('hello', 0) # 返回value. pop也可以指定不存在的返回值
print(a)
b = d.popitem() # 随机删除。d空会报错
print(b, d)

## 清空字典中所有元素
d.clear()
print(d)
# python中一切皆对象，每个对象都有bool值
print(bool(d), bool(()), bool([])) # 均为False

# Python3.11 新特性
# 字典并运算符 | 合并两个字典