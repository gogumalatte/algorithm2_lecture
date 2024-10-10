'''
https://www.acmicpc.net/problem/15726
문제: 이칙연산
난이도: 브론즈4
'''

a, b, c = map(int, input().split())

print(max(int(a * b / c), int(a / b * c)))
