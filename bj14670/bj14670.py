'''
https://www.acmicpc.net/problem/14670
문제: 병약한 영정
난이도: 실버4
'''

medicine_cnt = int(input())
medicine_box = []
for _ in range(medicine_cnt):
    medicine_box.append(list(map(int, input().split())))
disease_cnt = int(input())
disease_box = []
for _ in range(disease_cnt):
    disease_box.append(list(map(int, input().split())))
answer = []
for i in range(disease_cnt):
    cur = []
    for j in range(disease_box[i][0]):
        for k in range(medicine_cnt):
            if disease_box[i][j+1] == medicine_box[k][0]:
                cur.append(medicine_box[k][1])
    if len(cur) != disease_box[i][0]:
        answer.append(["YOU DIED"])
    else:
        answer.append(cur)
for i in range(disease_cnt):
    print(*answer[i])
