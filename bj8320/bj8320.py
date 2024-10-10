'''
https://www.acmicpc.net/problem/8320
문제: 직사각형을 만드는 방법
난이도: 브론즈2
'''
import math

def solve(num):
    sum = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += 1
    return sum

n = int(input())
answer = 0

for i in range(1, n+1):
    answer += solve(i)
    
print(answer)
