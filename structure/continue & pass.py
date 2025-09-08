# 求偶数的和
sum = 0
for i in range(1, 101):
    if i % 2:
        continue # 回到循环开头；for将i移动到序列的下一个
    sum += i
print(sum)

# 空语句pass：占位符，保留字，使不报错
# pass不会阻止下方内容执行
for i in range (10):
    pass
    print(i)

while True:
    pass