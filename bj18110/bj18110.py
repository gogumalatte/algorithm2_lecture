'''
https://www.acmicpc.net/problem/18110
'''

def myround(num):
    n = int(num)
    dot = num - n
    t = 0
    if dot >= 0.5:
        t = 1
    return (n + t)

import sys

index = int(input())

if index == 0:
    print(0)
else:
    dNum = myround(index * 0.15) # 절사할 15%의 크기
    box = {} # 딕셔너리로 저장, 1~30의 난이도 당 몇 명의 사람이 투표했는지 저장한다.

    # step1. 입력을 딕셔너리에 저장하고 난이도 순으로 정렬하는 단계
    for _ in range(index):
        a = int(sys.stdin.readline())
        if a in box:
            box[a] += 1
        else:
            box[a] = 1
    sorted_box = dict(sorted(box.items())) # 난이도 별로 정렬된 딕셔너리

    # step2. 가장 큰 값들, 작은 값들을 절사하는 단계
    curNum_f = 0 # 앞 쪽에서 키를 옮겨가며 절사하기 위해 현재 index를 저장해놓는 변수
    box_Keys_list = list(sorted_box.keys())
    for i in range(dNum):
        a = box_Keys_list[curNum_f]
        sorted_box[a] -= 1
        if sorted_box[a] == 0:
            curNum_f += 1

    curNum_b = len(sorted_box) - 1 # 뒤 쪽에서 키를 옮겨가며 절사하기 위해 현재 index를 저장해놓는 변수
    for i in range(dNum):
        a = box_Keys_list[curNum_b]
        sorted_box[a] -= 1
        if sorted_box[a] == 0:
            curNum_b -= 1

    # step3. 평균을 구하는 단계
    sum = 0
    for key, value in sorted_box.items():
        sum += key * value
    avg = myround(sum/(index - 2 * dNum))
    print(avg)
