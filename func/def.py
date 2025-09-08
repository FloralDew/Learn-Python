# 基础示例
def get_sum(end, begin = 1, step = 1): # 形参，begin/step默认值为1
    # 定义函数时，非默认值参数(end)必须在默认值参数之前
    s = 0
    for i in range(begin, end + 1, step):
        s += i
    return s # 可省略

## 传参
# 位置参数：调用时参数的个数/顺序必须和定义时相同
print(get_sum(10, 1, 1)) # 实参
# 关键字参数：顺序可以不一样.
print(get_sum(begin = 1, end = 10, step = 2))
# 关键字传参和位置传参混用时，位置传参必须在前面
print(get_sum(10, 1, step = 2))

# 带有默认值的函数可以不传那个参数
print(get_sum(10)) # 位置参数一定按照顺序传入，第一个就是第一个
# 想仅赋值后面的默认值参数时不可用逗号空出位置
# print(get_sum(10, ,2)) 报错
print(get_sum(10, step = 2)) # 跳过默认值参数后必须用关键字传参

## 可变参数
# 个数可变的位置参数(参数前加*)：函数调用时可接收任意个数的实参，并放到一个元组中
def fun1(*para):
    print('func activated')
    print(type(para))
    for i in para:
        print(i)

fun1('a', 2, 3, [5, '2'])
fun1([0, 1, 2]) # 元组中只有一个参数，就是这个列表
fun1(*[0, 1, '2']) # 将序列解包，即元组中有三个元素
fun1(0) # 是单个元素的元组
# 也可以单独使用fun1()不传参数，即空元组

# 个数可变的关键词参数(参数前加**)：函数调用时可接收任意多个key = value，并放入字典
def fun2(**kwpara):
    print(type(kwpara))
    for k, v in kwpara.items():
        print(k, '-->', v)

fun2(name = 'Mike', age = 10)
d = {str(k):k for k in range(10)} 
fun2(**d) # 将字典解包。注意字典的键必须是字符串类型

## 函数的返回值(默认为None)
# 多个返回值
def calc(*element):
    num_sum = 0
    num_product = 1
    for i in element:
        num_sum += i
        num_product *= i
    try:
        aver = num_sum / len(element)
    except ZeroDivisionError:
        aver = None
    return num_sum, aver, num_product

res = calc(1, 2, 3, 4)
print(type(res)) # <class 'tuple'>
print(res)
print(calc())

s, aver, p = calc(*range(1, 5)) # 解包赋值、解包range
print(s, aver, p)