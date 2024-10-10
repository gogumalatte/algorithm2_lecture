'''
https://www.acmicpc.net/problem/27918
문제: 탁구 경기
난이도: 브론즈4
'''
import sys

total_round = int(input())
dalgu = 0
ponix = 0
for _ in range(total_round):
    if abs(dalgu - ponix) >= 2:
        break
    winner = sys.stdin.readline().strip()
    if winner == 'D':
        dalgu += 1
    else:
        ponix += 1

print(f'{dalgu}:{ponix}')
