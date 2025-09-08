
# eval() literally, 去掉字符串中的引号
# 参数必须是字符串或装着字符串的变量
x = eval('3.14 + 3')
print(x, type(x))
# print(float('3.14 + 3')) # 报错

# eval() 经常与 input() 连用，获取输入的数值
age = eval(input("enter your age:"))
print(age, type(age))
# age 的类型取决于输入的是 float 还是 int
# 输入非数字会报错

hello = "Fudan University"
print(hello)
print(eval('''hello''')) # 也输出变量hello的内容
# 即便上一行eval里通过input读取用户输入的hello，也可以
# print(eval(hello)) # 报错

a = "hello"
print(eval(a)) # 套娃也可以

print(eval("0xa")) # 输出10
# print(eval(1)) # 报错