s1 = 'hello'
s2 = 'world'

## 字符串拼接
# (1)
print(s1 + s2)
# (2)
print(''.join([s1, s2])) # 使用空字符串作为分隔符进行连接
# join中可以是一个集合、列表、元组，但是由于集合的无序性，连接的字符串也无序
print('-'.join([s1, 'python', s2]))
# (3)
print('hello''the'
      'world')
# (4)
print('%s%s' % (s1, s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1, s2))

## 字符串去重
s = 'aaabbbbbccddddeeeffffghijjjk'
# (1)
new_s = ''
for i in s:
    if not i in new_s: # i not in new_s 也可
        new_s += i
print(new_s)
# (2)通过集合去重+列表排序操作
a = set(s)
lst = list(a)
print(lst)
lst.sort(key = s.index)
print(lst)
print(s.index, type(s.index))
print(''.join(lst))