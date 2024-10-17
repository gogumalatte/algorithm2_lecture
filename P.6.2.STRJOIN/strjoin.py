'''
문제: 문자열 합치기
'''
from heapq import heappush, heappop, heapify

def strjoin(strlen):
    heapify(strlen) # strlen을 최소힙(우선순위 큐)으로 구성
    ret = 0
    while len(strlen) > 1: # 원소가 하나 남을 때까지
        len1 = heappop(strlen)
        len2 = heappop(strlen)
        heappush(strlen, len1 + len2)
        ret += len1 + len2
    return ret

for _ in range(int(input())):
    n = int(input())
    strlen = list(map(int, input().split()))
    print(strjoin(strlen))
