'''
https://www.acmicpc.net/problem/2503
문제: 숫자 야구
난이도: 실버3
'''

answer_box = []
# 가능한 모든 경우의 수
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                answer_box.append(str(i*100 + j *10 + k))

three_strike = False

testCase = int(input())
for _ in range(testCase):
    num, s, b = map(str, input().split())
    this_case_box = []
    if s == '3': # 3스트라이크: 정답이 하나로 확정됨
        answer_box = [num]
        break
    elif s == '2': # 2스트라이크
        for i in range(1, 10):
            if num[0] != str(i):
                this_case_box.append(str(i)+num[1]+num[2])
            if num[1] != str(i):
                this_case_box.append(num[0]+str(i)+num[2])
            if num[2] != str(i):
                this_case_box.append(num[0]+num[1]+str(i))
    elif s == '1': # 1스트라이크
        # 1스트라이크 & 2볼
        if b == '2':
            this_case_box.append(num[0]+num[2]+num[1])
            this_case_box.append(num[2]+num[1]+num[0])
            this_case_box.append(num[1]+num[0]+num[2])
        # 1스트라이크 & 1볼
        elif b == '1':
            for i in range(1, 10):
                this_case_box.append(num[0]+num[2]+str(i))
                this_case_box.append(num[0]+str(i)+num[1])
                this_case_box.append(str(i)+num[1]+num[0])
                this_case_box.append(num[2]+num[1]+str(i))
                this_case_box.append(str(i)+num[0]+num[2])
                this_case_box.append(num[1]+str(i)+num[2])
        # 1스트라이크 & 0볼
        elif b == '0':
            for i in range(1, 10):
                for j in range(1, 10):
                    if str(i) != num[1] or str(j) != num[2] or str(i) != num[2] or str(j) != num[1]:
                        this_case_box.append(num[0]+str(i)+str(j))
                    if str(i) != num[0] or str(j) != num[2] or str(i) != num[2] or str(j) != num[0]:
                        this_case_box.append(str(i)+num[1]+str(j))
                    if str(i) != num[0] or str(j) != num[1]:
                        this_case_box.append(str(i)+str(j)+num[2])
    elif s == '0': # 0스트라이크
        # 0스트라이크 & 3볼
        if b == '3':
            this_case_box.append(num[1]+num[2]+num[0])
            this_case_box.append(num[2]+num[0]+num[1])
        # 0스트라이크 & 2볼
        if b == '2':
            for i in range(1, 10):
                this_case_box.append(str(i)+num[0]+num[1])
                this_case_box.append(str(i)+num[2]+num[0])
                this_case_box.append(str(i)+num[2]+num[1])
                this_case_box.append(num[1]+str(i)+num[0])
                this_case_box.append(num[2]+str(i)+num[0])
                this_case_box.append(num[1]+num[0]+str(i))
                this_case_box.append(num[1]+num[2]+str(i))
                this_case_box.append(num[2]+num[0]+str(i))
        # 0스트라이크 & 1볼
        if b == '1':
            for i in range(1, 10):
                for j in range(1, 10):
                    if str(i) != num[1] or str(j) != num[2] or str(i) != num[2] or str(j) != num[1]:
                        this_case_box.append(str(i)+num[0]+str(j))
                    if str(i) != num[1] or str(j) != num[2] or str(i) != num[2] or str(j) != num[1]:
                        this_case_box.append(str(i)+str(j)+num[0])
                    if str(i) != num[0] or str(j) != num[2] or str(i) != num[2] or str(j) != num[0]:
                        this_case_box.append(num[1]+str(i)+str(j))
                    if str(i) != num[0] or str(j) != num[2] or str(i) != num[2] or str(j) != num[0]:
                        this_case_box.append(str(i)+str(j)+num[1])
                    if str(i) != num[0] or str(j) != num[1] or str(i) != num[1] or str(j) != num[0]:
                        this_case_box.append(num[2]+str(i)+str(j))
                    if str(i) != num[0] or str(j) != num[1] or str(i) != num[1] or str(j) != num[0]:
                        this_case_box.append(str(i)+num[2]+str(j))
        # 0스트라이크 & 0볼
        if b == '0':
            for i in range(1, 10):
                for j in range(1, 10):
                    for k in range(1, 10):
                        if i != num[0] or i != num[1] or i != num[2] or j != num[0] or j != num[1] or j != num[2] or k != num[0] or k != num[1] or k != num[2]:
                            this_case_box.append(str(i)+str(j)+str(k))

    answer_box = list(set(answer_box) & set(this_case_box))
    print(answer_box)


print(len(answer_box))