# 提示文字不是必须的
# 无论输入什么，都返回字符串类型
name = input("请输入姓名")
print("My name is:",name)
print("My name is:"+name) # + 连接字符串

# 接受整数类型：int()函数
x = int(input("Your lucky number: "))
print('my lucky num:',x) # 不可使用+x，因为x是int型