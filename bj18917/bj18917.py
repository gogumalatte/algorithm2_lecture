'''
https://www.acmicpc.net/problem/18917
문제: 수열과 쿼리 38
난이도: 실버3
'''

# 리스트를 사용하면 시간초과 발생
# 리스트를 사용하지 않고, 문제를 풀 수 있는 방법 고민하기!!

import sys

sum = 0
xor = 0

index = int(input())
for _ in range(index):
    query = sys.stdin.readline().strip()
    if query[0] == '1':
        sum += int(query[2:])
        xor ^= int(query[2:])
    elif query[0] == '2':
        sum -= int(query[2:])
        xor ^= int(query[2:])
    elif query[0] == '3':
        sys.stdout.write(str(sum) + '\n')
    elif query[0] == '4':
        sys.stdout.write(str(xor) + '\n')
