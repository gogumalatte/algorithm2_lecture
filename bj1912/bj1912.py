'''
https://www.acmicpc.net/problem/1912
문제: 연속합
난이도: silver2
'''

index = int(input())
box = list(map(int, input().split()))

# 다이나믹 프로그래밍
curs, maxs = 0, -1000
for i in range(index):
    curs = max(curs, 0) + box[i]
    maxs = max(curs, maxs)

print(maxs)
