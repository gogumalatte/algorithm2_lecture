'''
https://www.acmicpc.net/problem/24314
문제: 알고리즘 수업 - 점근적 표기 2
난이도: 실버5
'''

a1, a2 = map(int, input().split())
c = int(input())
n = int(input())
answer = 1

for i in range(n, 101):
    if c * n > a1 * n + a2:
        answer = 0
        break

# 예외 조건
if a1 < c:
    answer = 0
print(answer)
