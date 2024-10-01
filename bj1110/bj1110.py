'''
https://www.acmicpc.net/problem/1110
문제: 더하기 사이클
난이도: 브론즈1
'''

num = int(input())
origin = num
answer = 0
sum = 0

while True:
    if num < 10:
        sum = num
    else:
        sum = (num // 10) + (num % 10)
    num = ((num % 10) * 10) + (sum % 10)
    answer += 1
    if origin == num:
        break

print(answer)
