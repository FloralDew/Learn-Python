# and or not
# and 和 or 从左向右结合，not 从右向左结合
print(True and False) # False
print(not 7 < 6) # True

print('-'*40)
print(7 > 6 or 10 / 0) # 除数为0会报错，但有短路效应