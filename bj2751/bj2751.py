'''
https://www.acmicpc.net/problem/2751
'''
import sys
index = int(sys.stdin.readline())
box = []

for _ in range(index):
    box.append(int(sys.stdin.readline()))

sorted_box = sorted(box)
for i in sorted_box:
    sys.stdout.write(str(i) + '\n')
