'''
https://www.acmicpc.net/problem/1181
'''

import sys
index = int(input())
box = []

for _ in range(index):
    box.append(sys.stdin.readline().rstrip('\n'))
    
unique_box = set(box)

sorted_box = sorted(unique_box, key = lambda s: (len(s), s))

for i in sorted_box:
    print(i)
