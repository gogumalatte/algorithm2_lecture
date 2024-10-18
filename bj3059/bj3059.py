'''
https://www.acmicpc.net/problem/3059
문제: 등장하지 않는 문자의 합
난이도: 브론즈3
'''

test_case = int(input())
total = sum(range(65, 91))
for _ in range(test_case):
    string = input()
    box = []
    for i in string:
        box.append(ord(i))
    print(total - sum(set(box)))
