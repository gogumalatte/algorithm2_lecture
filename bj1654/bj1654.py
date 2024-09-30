'''
https://www.acmicpc.net/problem/1654
문제: 랜선 자르기
난이도: 실버2
'''

# 이진 탐색으로 풀어야 됨!
import sys

line_num, need = map(int, input().split())
lines = []
for _ in range(line_num):
    lines.append(int(sys.stdin.readline()))

possible_max = int(sum(lines) / need)
index_min = 0
index_max = possible_max
answer = 0

while index_min <= index_max:
    sum = 0
    middle = (index_min + index_max) // 2
    if middle == 0:
        middle = 1
    
    for i in lines:
        sum += i // middle
    
    if sum >= need:
        index_min = middle + 1
    else:
        index_max = middle - 1
    
print(index_max)
