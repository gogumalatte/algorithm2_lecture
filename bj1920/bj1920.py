'''
https://www.acmicpc.net/problem/1920
'''

n = int(input())
box = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
answer = []

for i in check:
    if box & {i}:
        answer.append(1)
    else:
        answer.append(0)

for i in answer:
    print(i)
