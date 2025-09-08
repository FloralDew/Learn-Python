# 匿名函数lambda 参数列表(任意个):表达式(返回值)
s = lambda a, b : a + b # s表示匿名函数(s即MATLAB中的句柄)
# 在函数函数体只有一句代码且只有一个返回值时用以简化
print(type(s)) # <class 'function'>
# 调用匿名函数
print(s(10, 20))
print(s(20, 20))

# 进阶用法
# (1)列表取值
lst = [1, 2, 'a', 6]
for i in range(len(lst)):
    res = lambda x:x[i] # res函数：输入列表后返回列表元素
    print(res(lst))
print(lst)

# (2)作为sort的key 以及后面学到的filter/map的参数
student_score = [
    {'name':'Max', 'score':98},
    {'name':'Mike', 'score':100},
    {'name':'Bob', 'score':99},
    {'name':'Lily', 'score':68}
]
student_score.sort(key = lambda x:x.get('score'), reverse = True)
print(student_score)