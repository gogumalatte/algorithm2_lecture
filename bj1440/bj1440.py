'''
https://www.acmicpc.net/problem/1440
문제: 타임머신
난이도: 브론즈2
'''

string = input()

a = int(string[0:2])
b = int(string[3:5])
c = int(string[6:8])

box = [a, b, c]

answer = 0

if a > 59 or b > 59 or c > 59:
    print(0)
else:
    for i in box:
        if i >= 1 and i <= 12:
            answer += 2
    print(answer)
