# Python中有加强版switch

x = input("Give me a string: ")
match x:
    case '我':
        print('one') # 无需使用break
    case '你':
        print('two')
    case _: # 其他
        print('else')

y = eval(input("Give me a number: "))
match y:
    case 1:
        print('one') # 无需使用break
    case 2:
        print('two')
    case _: # 其他
        print('else')