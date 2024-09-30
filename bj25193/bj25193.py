'''
https://www.acmicpc.net/problem/25193
문제: 곰곰이의 식단 관리
난이도: 실버 5
'''

index = int(input())
string = input()

chicken = 0

for i in string:
    if i == 'C':
        chicken += 1

answer = chicken/(index-chicken + 1)

if answer - int(answer) > 0:
    print(int(answer) + 1)
else:
    print(int(answer))
