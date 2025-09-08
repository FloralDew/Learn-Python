# 与list不同，元组是不可变序列，不可增删改
# 元组比列表的访问和处理速度更快
# 元组可以作为字典的键，列表不可以

## 创建元组：()
t = ("hello", [10, 20, 30], 50.0, "python") # 不会拆开list
print(t)
t = tuple('hello') # 拆开成单个字母
print(t)
t = (["1", 2, 3, 4])
print(t) # ([])会把list中的转到tuple中
t = 10.0, 20, 30, 40 # 括号可省略
print(t, type(t)) # <class 'tuple'>

# 元组生成式
tp = (i for i in range(1, 4))
print(tp) # 现在tp只是一个生成器对象
tp = tuple(tp) # 转换成元组
print(tp)

tp2 = (i for i in range(1, 21) if not i % 5) # 5, 10, 15, 20
print(tp2.__next__()) # 可以取出生成器对象的内容
print(tuple(tp2)) # 只剩(10, 15, 20)

print(t)
print(10 in ("10", 11)) # False
print(max(t))
print(len(t))
print(t.index(10)) # 0
print(t.count(10))
# index/count对10和10.0不区分

t = () # type(t)为tuple
t = (10) # type(t)为int：只有一个元素时逗号不能省
t = (10,) # type(t)为tuple
lst = [] # type(lst)为list
lst = [10] # type(lst)为list
lst = [10,] # type(lst)为list

## 删除元组
del t
# print(t) # NameError: name 't' is not defined.

## 元组元素的访问与遍历
t = ('python', '10', 75, [10.0], (8,))
print(t[::2])

for item in t:
    print(item)

for index in range(len(t)): # range第一个参数缺省为0
    print(t[index])

for index, item in enumerate(t, 0):
    print(index, '\t', item)
