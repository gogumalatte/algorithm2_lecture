'''
https://www.acmicpc.net/problem/27065
문제: 2022년이 아름다웠던 이유
난이도: 브론즈1
'''

import math
index = int(input())

for _ in range(index):
    box = [1]
    year = int(input())
    for i in range(2, int(math.sqrt(year)) + 1):
        if year % i == 0:
            box.append(i)
            box.append(int(year/i))
    set_box = list(set(box))
    if sum(set_box) <= year:
        print("BOJ 2022")
    else:
        check = True
        for j in box:
            small_box = [1]
            for k in range(2, int(math.sqrt(j)) + 1):
                if j % k == 0:
                    small_box.append(k)
                    small_box.append(int(j/k))
            if j < sum(list(set(small_box))):
                check = False
        if check == True:
            print("Good Bye")
        else:
            print("BOJ 2022")
