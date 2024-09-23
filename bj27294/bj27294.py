'''
https://www.acmicpc.net/problem/27294
'''

time, alchol = map(int, input().split())

if (time>= 12 and time <= 16) and alchol == 0:
    print(320)
else:
    print(280)