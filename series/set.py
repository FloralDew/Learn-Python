# 无序、不重复
# 内部元素只能是不可变数据类型
# set/dict/list都是可变数据类型

## 创建集合
s = {10, 20, 30, 40}
print(s)
# s = {[10]} # 报错 unhashable type: 'list'
print(type({})) # {}代表空字典
print(type({10})) # 仍是集合

s = set() # 空集合的bool值也是False
print(s, type(s)) # set()才是空集合

s = set('abcabcabc')
print(s) # 无序、不重复
s2 = set([1, 2, 3])
print(s2) # 列表变集合
s3 = set(range(10))
print(s3)

# 集合生成式
s2 = {i ** 2 for i in range(1, 10) if not i % 2}
print(s2)

# 集合属于序列的一种，max(), max(), len(), (not) in, .index(), .count()均可

## 集合的删除
del s2
# print(s2) # 报错

## 集合的操作符 -> 得到的也是集合
# A & B 交
# A | B 并
# A - B 差
# A ^ B 交集以并集为全集的补集

## 其他操作
s.add('a') # 重复的话不会添加
print(s)
s.add('d')
print(s)
s.remove('b') # 不存在会报错
print(s)
s.clear()
print(s) # set()


for item in s3:
    print(item, end = ' ')
print(item) # s3不能是空集

for i, item in enumerate(s3, start = 1):
    print(i, '->', item)