# 内置模块: 随python解释器自动一同安装的模块, 大致有270个
## random
'''
seed()初始化随机种子 默认为当前系统时间
random()生成[0, 1)间随机数
randint() [a, b]间随机整数
randrange() [m, n) 步长为k
uniform() [a, b]间随机小数
choice(seq) 随机选择一个元素
shuffle(seq) 返回打乱后的序列
'''
import random
random.seed(1)
print(random.random())
print(random.random()) # 两次运行结果相同(这两个不同, 但是两次运行相同)
print(random.randint(1, 10))
for i in range(10):
    print(random.randrange(1, 22, 3)) # 只有1, 4, 7, ..., 19
print(random.uniform(1, 100))
lst = [i for i in range(11)]
print(random.choice(lst))
random.shuffle(lst)
print(lst)