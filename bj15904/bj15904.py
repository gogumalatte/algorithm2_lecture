'''
https://www.acmicpc.net/problem/15904
문제: UCPC는 무엇의 약자일까?
난이도: 실버5
'''
import sys

string = list(sys.stdin.readline().strip())
is_UCPC = []

for letter in string:
    if letter == 'U' and len(is_UCPC) == 0:
        is_UCPC.append(letter)
    if letter == 'C' and len(is_UCPC) == 1:
        is_UCPC.append(letter)
    if letter == 'P' and len(is_UCPC) == 2:
        is_UCPC.append(letter)
    if letter == 'C' and len(is_UCPC) == 3:
        is_UCPC.append(letter)

if is_UCPC == ['U', 'C', 'P', 'C']:
    print("I love UCPC")
else:
    print("I hate UCPC")
