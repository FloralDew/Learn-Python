# 之前写过的都是顺序结构，接下来学习选择结构

number = eval(input("请输入您的4位验证码")) # input 字符串去掉外面的引号(输入直接影响到代码层面)
# 注意这一句不输入会报错，相当于number =
# 输入字符串也会报错，相当于number = xxx，但xxx是未定义的变量
# 输入"xxx"不会报错，相当于number = "xxx"，因为eval去掉了字符串外面套的引号
if number == 1234: print('Congratulations!')
else: print('Sorry, incorrect')
# 语句块只有一句，可以放到冒号后面；否则必须缩进

# 注意 if 和 : 之间会被转换为bool值。如
# 判断输入的是否是空字符串
if input("Enter a string: "): # 非空字符串的bool为True
    print("Not empty")
else:
    print("Empty!")

# 判断是否为偶数
if not eval(input("Enter an integer: ")) % 2: # 0 的bool值为False
    print("even")
    a = 5 # if 内也可以直接定义变量，但是 if 和 : 之间的条件不行

# 条件表达式：当if和else都只有一个语句时可以用于简化
res = 10 if 5 == 5 else 100
# res = 5 == 5 ? 10 : 100 # 相当于C中的这个
print(res)

# 或者
print(10 if 5 == 5 else 100)

# 多分支结构
score = eval(input('Enter your grades: '))
if score > 90: # 注意 Python支持 90 < score <= 100的语法！
    print('Excellent!')
elif score > 80:
    print('Great')
elif score > 70:
    print('Good')
else:
    print('Better next time!')

# 嵌套

# 多个条件用 and or 连接