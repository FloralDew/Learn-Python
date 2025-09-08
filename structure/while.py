# while：无限循环 条件是布尔值
while input("enter Y to continue: ") == 'Y':
    print("You entered Y")
print("The loop was ended.")

i = 0 # (1)初始化变量
sum = 0
while i <= 100: # (2)条件判断
    sum += i # (3)语句块
    i += 1 # (4)改变变量。Python没有i++
else: # 循环正常结束
    print('sum =', sum)

# 循环嵌套