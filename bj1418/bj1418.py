'''
https://www.acmicpc.net/problem/1418
문제: K-세준수
난이도: 실버5
'''

n = int(input())
k = int(input())
answer = 0
for i in range(1, n + 1):
    num = i
    insu = 2
    while insu <= k:
        if num % insu == 0:
            num = num // insu
        else:
            insu += 1
        if num == 1:
            break

    if num == 1:
        answer += 1

print(answer)
