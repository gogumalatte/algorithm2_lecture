'''
https://www.acmicpc.net/problem/17093
문제: total circle
난이도: 브론즈1
'''
import sys

n, m = map(int, sys.stdin.readline().split())
pBox = []
qBox = [] # q의 점들 중 하나를 기준으로 p의 모든 점들을 포함하는 원의 최소 반지름을 얻어야함.
circle_min = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    pBox.append([x, y])
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    qBox.append([x, y])
    
for i in range(m):
    now = 0
    for j in range(n):
        now = max(now, (qBox[i][0] - pBox[j][0])**2 + (qBox[i][1] - pBox[j][1])**2)
    circle_min = max(now, circle_min)
print(circle_min)
