'''
https://www.acmicpc.net/problem/23278
문제: 영화 평가
난이도: 브론즈1
'''

n, l, h = map(int, input().split())
box = list(map(int, input().split()))

sorted_box = sorted(box)
avg = sum(sorted_box[l: n-h])/(n - l - h)

print(avg)