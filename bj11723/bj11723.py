'''
https://www.acmicpc.net/problem/11723
문제: 집합
난이도: 실버5
'''
import sys

S = { }
for i in range(1, 21):
    S[i] = 0

index = int(input())
for _ in range(index):
    box = sys.stdin.readline().strip()
    if box[0:3] == "add":
        if S[int(box[4:])] == 0:
            S[int(box[4:])] = 1
    elif box[0:6] == "remove":
        if S[int(box[7:])] == 1:
            S[int(box[7:])] = 0
    elif box[0:5] == "check":
        if S[int(box[6:])] == 1:
            print(1)
        else:
            print(0)
    elif box[0:6] == "toggle":
        if S[int(box[7:])] == 1:
            S[int(box[7:])] = 0
        else:
            S[int(box[7:])] = 1
    elif box[0:3] == "all":
        for i in range(1, 21):
            S[i] = 1
    elif box[0:5] == "empty":
        for i in range(1, 21):
            S[i] = 0
