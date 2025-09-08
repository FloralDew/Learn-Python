# > < == != >= <= 返回布尔值True/False

print(100 < 99) # False
print(70 >= 70) # True
print("我啊" == '我啊') # True
print("我" == '你') # False

# 注意 Python支持 90 < score <= 100的语法！更加贴合常识
print(1 < 2 < 2) # C会判断为真。Python判断为假
print(1 < 2 < 3) # True
print(2 <= 2 < 3 < 4 > 3) # True
print(2 <= 2 < 3 < 4 > 5) # False