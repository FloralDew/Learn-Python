# for：遍历循环
# 遍历字符串
for i in 'hello': # 第一次循环：定义 + 赋值'h'，i在for外面可见
    print(i, end = ' ')
# 注意，如果for一次也不执行，i不会被定义，外面引用i会报错！
print(i) # 正确，i 为'o'

# range()函数：创建一个[n, m)的整数序列
# r = range(5)
# print(r, type(r)) # range(0, 5) <class 'range'>
for i in range(1, 11):
    if not i % 2:
        print(i, 'is even')

# 判断100 - 999之间的水仙花数
for i in range(100, 1000):
    sum = 0 # 必须，否则sum += 会报错
    for j in range(0, 3):
        sum += int(str(i)[j]) ** 3
    if i == sum:
        print(i, '是水仙花数')
else:
    print("循环正常结束")

# for...else...结构：循环正常结束(指没有被break)，执行else部分
# for与while的区别：会自动将i移到序列的下一个