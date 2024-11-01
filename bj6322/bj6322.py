'''
https://www.acmicpc.net/problem/6322
문제: 직각 삼각형의 두 변
난이도: 브론즈3
'''
import math
index = 0

while True:
    a, b, c = map(int, input().split())
    index += 1
    if a == 0 and b == 0 and c == 0:
        break
    print(f'Triangle #{index}')
    if a == -1:
        if c**2 > b**2:
            answer = math.sqrt(c**2 - b**2)
            print(f"a = {answer:.3f}")
        else:
            print("Impossible.")
    elif b == -1:
        if c**2 > a**2:
            answer = math.sqrt(c**2 - a**2)
            print(f"b = {answer:.3f}")
        else:
            print("Impossible.")
    elif c == -1:
        answer = math.sqrt(a**2 + b**2)
        print(f"c = {answer:.3f}")
    print("")