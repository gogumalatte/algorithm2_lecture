'''
https://www.acmicpc.net/problem/1764
문제: 듣보잡
난이도: 실버4
'''
import sys

no_listen, no_see = map(int, input().split())
box = {}
answer = []

for i in range(no_listen):
    string = sys.stdin.readline().strip()
    box[string] = 1

for i in range(no_see):
    string = sys.stdin.readline().strip()
    if string in box:
        answer.append(string)

sorted_answer = sorted(answer)
print(len(answer))
for i in sorted_answer:
    print(i)
