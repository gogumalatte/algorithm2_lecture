'''
https://www.acmicpc.net/problem/30802
'''

import math

num = int(input())
size = map(int, input().split())
t, p = map(int, input().split())
sum = 0

for i in size:
    sum += math.ceil(i/t)
print(sum)
print(num // p, num % p)
