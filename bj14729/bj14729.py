'''
https://www.acmicpc.net/problem/14729
문제: 칠무해
난이도: 실버5
'''
import sys

box = []
index = int(input())

for i in range(index):
    num = float(sys.stdin.readline())
    if i < 7:
        box.append(num)
    else:
        if max(box) > num:
            for j in range(len(box)):
                if box[j] == max(box):
                    box[j] = num
                    break

for i in sorted(box):
    print(f"{i:.3f}")
