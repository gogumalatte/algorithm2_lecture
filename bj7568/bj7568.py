'''
https://www.acmicpc.net/problem/7568
'''

index = int(input())
box = []
for _ in range(index):
    w, h = map(int, input().split())
    box.append([w,h,0])

for i in range(index):
    rank = 1
    for j in range(index):
        if box[i][0] < box[j][0] and box[i][1] < box[j][1] and i != j:
            rank += 1
    box[i][2] = rank

for i in range(index):
    print(box[i][2])
