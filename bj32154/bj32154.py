'''
https://www.acmicpc.net/problem/32154
문제: SUAPC 2024 Winter
난이도: 브론즈5
'''

first = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'M']
second = ['A',  'C', 'E', 'F', 'G', 'H', 'I','L', 'M']
third = ['A', 'C',  'E', 'F', 'G', 'H', 'I', 'L', 'M']
forth = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'L', 'M']
fifth = ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']
sixth = ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']
seventh = ['A', 'C',  'E', 'F', 'G', 'H', 'L', 'M']
eightth = ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']
nineth = ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']
tenth = ['A', 'B', 'C', 'F', 'G', 'H', 'L', 'M']

num = int(input())

match (num):
    case 1:
        print(len(first))
        print(*first)
    case 2:
        print(len(second))
        print(*second)
    case 3:
        print(len(third))
        print(*third)
    case 4:
        print(len(forth))
        print(*forth)
    case 5:
        print(len(fifth))
        print(*fifth)
    case 6:
        print(len(sixth))
        print(*sixth)
    case 7:
        print(len(seventh))
        print(*seventh)
    case 8:
        print(len(eightth))
        print(*eightth)
    case 9:
        print(len(nineth))
        print(*nineth)
    case 10:
        print(len(tenth))
        print(*tenth)
