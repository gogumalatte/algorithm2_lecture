'''
C번 - ANA는 회문이야
'''

index = int(input())
string = input()

box = []

for i in range(index):
    if string[i] == "A":
        box.append(i)

cur = 0
answer = 0

while cur < len(box) - 1 :
    n_num = 0
    for i in range(box[cur], box[cur+1], 1):
        if string[i] == 'N':
            n_num += 1
    if n_num == 1:
        answer += 1
    cur += 1

print(answer)
