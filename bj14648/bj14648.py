'''
https://www.acmicpc.net/problem/14648
문제: 쿼리 맛보기
난이도: 브론즈2
'''

n, q = map(int, input().split())
box = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0]  == 1:
        print(sum(box[query[1]-1: query[2]]))
        temp = box[query[1] - 1]
        box[query[1] -1] = box[query[2] -1]
        box[query[2]-1] = temp
    elif query[0] == 2:
        first = sum(box[query[1]-1: query[2]])
        second = sum(box[query[3]-1: query[4]])
        print(first-second)