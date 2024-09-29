'''
A번 - 햄버거정렬
'''

string = input()

match (string):
    case '(1)':
        print(0)
    case '()1':
        print(1)
    case '1()':
        print(1)
    case '1)(':
        print(1)
    case ')1(':
        print(2)
    case ')(1':
        print(1)
