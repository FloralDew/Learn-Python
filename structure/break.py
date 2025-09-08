# break在while循环中的使用
i = 3
while i > 0:
    if input("Enter your password: ") == '0721':
        print('correct!')
        break
    i -= 1
    print("incorrect!", i, 'times left')
else: # break结束不会执行else
    print("plz try 3 mins later.")

# break在for循环中的使用
for i in 'hello':
    if i == 'l':
        break
    print(i)