# 列表：一系列按特定顺序排列的元素组成，是可变序列
# int float str 都是不可变数据类型，即字符串是不可变序列

## 列表的创建
lst = ['hello', 'world', 98, 100.5, True]
print(lst)
lst2 = list("helloworld") # 会把每个字符分开
print(lst2)
lst3 = list(range(1, 10, 2)) # 1, 3, 5, 7, 9
print(lst3)

## 列表生成式
lst4 = [item for item in range(1, 11)] # item只是个变量，可以是别的标识符。这里的item在外部不可见
print(lst4)
lst4 = [item ** 2 for item in range(1, 11)]
print(lst4)
# item可以仅用于计数
import random
lst4 = [random.randint(1, 100) for _ in range(1, 11)] # 产生[1, 100]随机整数10次，不使用_这个变量
print(lst4)
# 加条件
lst4 = [item for item in range(1, 11) if item % 2] # 1, 3, 5, 7, 9
print(lst4)

## 列表是序列的一种，对序列的操作符、运算符、函数都可使用
print(lst + lst2)
print(id(lst + lst2))
print(id(lst + lst2))
# 以上两个东西的id不一样。不可变是对一个list而言的，组合不算
print(lst * 2)
print(len(lst))
print(lst[: 5 : 2]) # ['hello', 98, True]，依然是list类型
# print(max(lst)) # 报错，int和str不能比大小 如果是字符串比大小，先比较首位ASCII，以此类推
print(min(lst3))
print(lst.index(1)) # 不报错，将True当1处理
print(lst2.count('o'))
print(lst3.index(5))


## 列表的删除操作
del lst2
# print(lst2) # NameError: name 'lst2' is not defined.


## 列表的遍历操作
for item in lst:
    print(item)

for i in range(0, len(lst)):
    print(i, '-->', lst[i])

for num, item in enumerate(lst, start = 1): # start缺省为0, start = 可以省略
    print(num, item) # num是序号，可以自己修改，不是索引


## 列表的特有操作
# 在末尾增加元素
print("before appending: ", lst, id(lst))
lst.append(True)
print("after appending: ", lst, id(lst))
# 可变数据类型：元素改变，但地址不变

# 在index索引位置插入元素object insert(index, object)
lst.insert(1, True)
print(lst)

# 删除元素
lst.remove(True) # 只会删除左数第一个
print(lst)
# 使用pop(index)根据索引将元素取出，再删除
print(lst.pop(1))
print(lst)

# 反向输出
lst.reverse() # 返回None
print(lst)

# 清空所有元素
lst3.clear() # 依然不改变id
print(lst3)

# 列表的拷贝
newlst = lst.copy() # 深拷贝
print(lst, id(lst))
print(newlst, id(newlst)) # id不同，元素相同
# 浅拷贝：直接使用list1 = list2, id相同，改变元素会同步改变

# 列表元素的修改：根据索引修改，没有方法
lst[1] = 'modified'
print(lst)

## 列表的排序操作
lst = [50, 56, 1, -8, 8, 99]
print("original: ", lst)

lst.sort() # 默认是升序
print("ascend: ", lst)
lst.sort(reverse = True) # 降序
print("descend: ", lst)

# 字符串的排序：首位ASCII，相同则看第二位，...
lst2 = ['banana', 'apple', 'Cat', 'Orange']
lst2.sort()
print("ascend: ", lst2)

# 忽略大小写进行比较：全部转换为小写
# key: 传入一个函数(句柄)，将在排序前作用于每个元素
lst2.sort(key = str.lower, reverse = False) # lower不加括号
print("ascend: ", lst2)

# 使用sorted函数，排序会创建新列表
asc_lst = sorted(lst)
print(asc_lst)
desc_lst = sorted(lst, reverse = True)
print(desc_lst)
# 也可以对字符串排序


## 二维列表
lst = [
    ['city', 'born rate'],
    ['SH', 10],
    ['BJ', 50]
]
print(lst)

# 二维列表的列表生成式
# 内部是关于行的，外部是关于列的
# 即for前面是元素，for后面是元素的生成方式
lst2 = [[j for j in range (i, i + 5)] for i in range(1, 1 + 5)]

# 二维列表的遍历
for row in lst2:
    for col in row:
        print(col, end = '\t')
    print() # 换行
