'''
https://www.acmicpc.net/problem/10989
'''

import sys
index = int(sys.stdin.readline())
box = [0] * 10001

for _ in range(index):
    a = int(sys.stdin.readline())
    box[a] += 1

for i in range(10001):
    if box[i] != 0:
        for _ in range(box[i]):
            sys.stdout.write(str(i) + '\n')
