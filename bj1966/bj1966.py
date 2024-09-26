'''
https://www.acmicpc.net/problem/1966
문제: 프린터 큐
난이도: 실버3
'''

def myQueue(n, m, box):
    cur = 0 # 현재 위치를 가리키는 변수
    answer = 0 # pop된 횟수, 즉 m이 pop되었을 때 값이 정답!
    while True:
        high_in_box = max(box)
        if box[cur] >= high_in_box and box[cur] != 0:
            box[cur] = 0
            answer += 1
        cur = (cur + 1 ) % n
        if box[m] == 0:
            break
    print(answer)

for _ in range(int(input())):
    n, m = map(int, input().split())
    box = list(map(int, input().split()))
    myQueue(n, m, box)
