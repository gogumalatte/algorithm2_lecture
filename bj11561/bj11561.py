'''
https://www.acmicpc.net/problem/11651
'''

index = int(input())
box = []
for _ in range(index):
    x, y = map(int, input().split())
    box.append([x, y])

sorted_box = sorted(box, key=lambda x: (x[1], x[0]))

for i in range(index):
    print(sorted_box[i][0], sorted_box[i][1])
