'''
https://www.acmicpc.net/problem/10773
'''
import sys

index = int(input())

box = []
for _ in range(index):
    a = int(sys.stdin.readline())
    if a == 0:
        box.pop()
    else:
        box.append(a)

print(sum(box))
