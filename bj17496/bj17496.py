'''
https://www.acmicpc.net/problem/17496
문제: 스타후르츠
난이도: 브론즈3
'''

summer, grow, index, cost = map(int, input().split())

answer = ((summer - 1) // grow ) * index * cost

print(answer)
