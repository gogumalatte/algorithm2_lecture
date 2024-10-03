'''
https://www.acmicpc.net/problem/11945
문제: 뜨거운 붕어빵
난이도: 브론즈4
'''

rows, cols = map(int, input().split())
reverse_bung = []

for _ in range(rows):
    a = list(map(str, input()))
    a.reverse()
    reverse_bung.append(a)

for i in range(rows):
    print("".join(reverse_bung[i]))
