try:
    num1 = float(input('enter a num: '))
    num2 = float(input('enter a num: '))
    res = num1 / num2
# except捕获try中的异常
# 异常捕获时先子类后父类，最后写最大的异常类型BaseException
except ZeroDivisionError:
    print('can\'t be devided by 0')
except ValueError:
    print('can\'t convert your str to num')
except BaseException:
    print('other error')
else: # try的部分都没有出现异常。可以省略
    print('res =', res)
finally: # 无论是否产生异常都执行。可以省略
    print('End.')