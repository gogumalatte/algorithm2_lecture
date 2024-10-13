'''
https://www.acmicpc.net/problem/10163
문제: 색종이
난이도: 브론즈1
'''
import sys

n = int(sys.stdin.readline())
box = [[0] * 1001 for _ in range(1001)]
answer = [0] * (n + 1)  # 각 색종이의 면적을 저장할 리스트

for idx in range(1, n + 1):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(a, a + c):
        for j in range(b, b + d):
            box[i][j] = idx  # 각 좌표에 색종이 번호 기록

# 면적 계산
for i in range(1001):
    for j in range(1001):
        if box[i][j] != 0:
            answer[box[i][j]] += 1  # 각 색종이의 면적 카운트

# 출력
for i in range(1, n + 1):
    print(answer[i])
