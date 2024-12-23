'''
https://www.acmicpc.net/problem/2309
문제: 일곱 난쟁이
난이도: 브론즈1
'''

box = []
for i in range(9):
    box.append(int(input()))
sum_box = sum(box)
sorted_box = sorted(box)
first, second = 0, 0

for i in range(9):
    for j in range(i + 1, 9):
        if sorted_box[i] + sorted_box[j] == sum_box - 100:
            first = i
            second = j

for i in range(9):
    if i != first and i != second:
        print(sorted_box[i])
