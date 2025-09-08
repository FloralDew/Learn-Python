# 内置函数：不需要前缀就可以直接使用的函数

## 数据类型转换函数
# bool()    int()   float()
# str()     tuple() list()  dict()  set()

## 数学函数
# abs()     max()   min() 
# divmod()  返回元组(商,余数)
# sum()     计算可迭代序列的和(多元素数值元组、列表)
# print(sum(1)) # 'int' object is not iterable
# pow()     求幂
# round(num, digit = 0) 四舍六入五成双
print(round(389.25, 1)) # 389.2
print(round(389.251, 1)) # 389.3
print(round(389.25)) # 389
print(round(389.25, -1)) # 390.0 即到十位
print(round(389.25, -2)) # 400.0

## 迭代器操作函数
lst = [5, 7, 98, 65, 32, 45]
# (1)sorted 排序
asc_lst = sorted(lst)
desc_lst = sorted(lst, reverse = True)
print(asc_lst, desc_lst)

# (2)reversed 反向
new_lst = reversed(lst)
print(type(new_lst)) # 结果是迭代器对象
new_lst = list(new_lst)
print(new_lst)

# (3)zip(iter1, iter2)打包成元组并返回可迭代的zip object对象

# (4)enumerate 将迭代器对象转换为(序号，值)的迭代器对象
enum = enumerate(lst, start = 1)
print(type((enum)))
enum = tuple(enum) # list也可
print(enum)

# (5)all(iter) 判断迭代器对象是否全为True
print(all([1, 2, 5, ()])) # False

# (6)any 判断迭代器对象是否至少有一个True

# (7)next(iter) 取出迭代器对象的下一个
zipobj = zip(tuple(range(2)), tuple('ab'))
print(next(zipobj)) # (0, 'a')
print(next(zipobj)) # (0, 'a')
# print(next(zipobj)) # StopIteration

# (8)filter(func, iter) 按照func中的条件筛选iter，
# 将所有为True的打包为迭代器对象返回
obj = filter(lambda x : True if x % 2 else False, range(10))
print(list(obj)) # [1, 3, 5, 7, 9]

# (9)map(func, iter) 通过func对iter操作后返回新的迭代器对象
t = ('apple', 'banana')
obj2 = map(lambda x : x.upper(), t)
print(list(obj2))
# 当t中有不具有upper()方法的元素时会报错AttributeError
# 容易发现，Python十分灵活，根据输入编译代码

## 其他函数
# (1)format(object, 格式字符串) 注意不是字符串的format方法
print(format(3.14, '20')) # 数值型默认右对齐
print(format('hello', '20')) # 字符串默认左对齐
print(format('hello', '*>20')) # *表示填充符，缺省为空格；>表示右对齐
print(format('hello', '^20')) # 居中对齐
print(format(3.135, '.2f')) # 3.13
print(round(3.135, 2)) # 3.13 ? 有时候不是五成双？
print(format(20, 'b')) # 10100
print(format(20, 'o')) # 八进制。大写O不行
print(format(58, 'x')) # 3a
print(format(58, 'X')) # 3A

# len(s) id(obj) 内存地址 type(x) eval(s)