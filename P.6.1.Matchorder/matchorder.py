'''
문제: 출전 선수 정하기
'''
from bisect import bisect_left

def matchorder(n, russian, korean):
    korean.sort() #한국 선수의 레이팅을 오름차순으로 정렬
    wins = 0
    for i in range(n):
        if korean[-1] < russian[i]: #가장 레이팅이 높은 한국 선수가 이길 수 없는 경우
            korean.pop(0) # 가장 레이팅이 낮은 선수를 버린다. 줄건 줘~
        else: # 이 외의 경우
            wins += 1 # 이길 수 있는 선수 중 레이팅이 낮은 선수를 출전. 가성비
            korean.pop(bisect_left(korean, russian[i]))
    return wins

for _ in range(int(input())):
    n = int(input())
    russian = list(map(int, input().split()))
    korean = list(map(int, input().split()))
    print(matchorder(n, russian, korean))
