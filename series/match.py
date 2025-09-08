# 结构模式匹配

data = eval(input('enter : '))
match data: # case后面的任何变量都用于匹配
    case {1 : 'cat'}:
        print('specific dict')
    case {1 : 'cat'}: # 不会执行。默认第一个
        print('second')
    case [a, b]:
        print('two-element list')
        print(a, b)
    case []:
        print('empty list')
    case ():
        print('tuple')
    case _: # _可以换成任何标识符，此case只能放在最后
        print('others')

# 同步迭代
for k, v in zip(tuple(range(5)), list('ABCDE')):
    match k, v:
        case 0, 'A':
            print('matched')
