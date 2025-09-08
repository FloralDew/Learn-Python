# 使用raise关键字抛出异常
try:
    gender = input('Enter your gender: ')
    if gender != 'M' and gender != 'F':
        raise Exception('Not available')
except Exception as e: # Exception是用户定义的异常
    print(e)
a = 10
int('a')
# Python中的常见异常类型
# ZeroDivisionError 除数为0
# IndexError        索引超限
# KeyError          不存在键
# NameError         未定义变量名
# SyntaxError       Python语法错误
# ValueError        值传入异常: int('str')
# AttributeError    属性或方法(.)不存在: ''.aaaaa
# TypeError         类型不合适: 'str' + 1
# IndentationError  缩进错误
# UnboundLocalError
# KeyboardInterrupt