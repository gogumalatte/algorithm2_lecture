'''
https://www.acmicpc.net/problem/10817
문제: 세 수
난이도: 브론즈3
'''

box = map(int, input().split())

sorted_box = sorted(box, reverse=True)

print(sorted_box[1])