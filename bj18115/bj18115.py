'''
https://www.acmicpc.net/problem/18115
문제: 카드 놓기
난이도: 실버3
'''

import sys
from collections import deque

# 이미 쌓여 있는 숫자 카드들(1, 2, 3... 순서)의 초기 상태를 역추적해야 하므로,
# skill의 순서도 거꾸로 생각해야 함!
# 예를 들어, 1은 맨 마지막에 skill로 인해 젤 위에 쌓임
N = int(sys.stdin.readline())
skill = list(map(int, sys.stdin.readline().split()))
skill.reverse()

dq = deque()
for i in range(N):
    if skill[i] == 1:
        dq.appendleft(i + 1)
    elif skill[i] == 2:
        dq.insert(1, i + 1)
    elif skill[i] == 3:
        dq.append(i + 1)

for i in dq:
    print(i, end=" ")