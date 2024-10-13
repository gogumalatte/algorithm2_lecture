'''
https://www.acmicpc.net/problem/4150
문제: 피보나치 수
난이도: 브론즈1
'''

n = int(input())
a = 1
b = 1
answer = 0

if n == 0:
    print(0)
elif n <= 2:
    print(1)
else:
    for i in range(3, n+1):
        answer = a + b
        a = b
        b = answer
    print(answer)