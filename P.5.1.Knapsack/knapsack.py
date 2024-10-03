'''
여행 짐싸기 문제: 메모이제이션으로 해결하기
'''

def packing(i, capacity):
    global n, w, p, cache
    if i == n or capacity <= 0:
        return 0
    elif cache[i][capacity] != -1:
        return cache[i][capacity]
    else:
        # capacity가 현재 아이템의 무게보다 작은 경우 아이템을 선택하지 않음
        drop = packing(i + 1, capacity)
        if capacity < w[i]:
            cache[i][capacity] = drop
        else:
            pick = packing(i + 1, capacity - w[i]) + p[i]
            cache[i][capacity] = max(drop, pick)
        return cache[i][capacity]

def reconstruct(i, capacity):
    global n, items, w
    if i == n:
        return []
    elif packing(i, capacity) == packing(i + 1, capacity):
        return reconstruct(i + 1, capacity)  # 현재 아이템을 선택하지 않음
    else:
        # 현재 아이템을 선택하는 경우
        return [items[i][0]] + reconstruct(i + 1, capacity - w[i])

# 입력 처리 및 메인 로직
for _ in range(int(input())):
    n, W = map(int, input().split())  # 아이템의 수와 배낭의 최대 무게
    items = [input().split() for _ in range(n)]  # 아이템 리스트 (이름, 무게, 가치)
    w = [int(items[i][1]) for i in range(n)]  # 무게 리스트
    p = [int(items[i][2]) for i in range(n)]  # 가치 리스트
    cache = [[-1] * (W + 1) for _ in range(n + 1)]  # 캐시 초기화
    
    # 최대 가치 계산
    optval = packing(0, W)
    
    # 최적 해 복원
    optsol = reconstruct(0, W)
    
    # 결과 출력
    print(optval, len(optsol))  # 최대 가치와 선택한 아이템의 수
    print(*optsol, sep='\n')  # 선택한 아이템 이름 출력
