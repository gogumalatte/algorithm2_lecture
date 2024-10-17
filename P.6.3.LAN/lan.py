'''
문제: lan
가중치가 있는 무방향 연결 그래프에서 가중치의 합이 가장 작은 스패닝 트리를 찾는 문제
'''
import math

def lan(n,w):
    dist = [w[0][i] for i in range(n)] # 출발 정점은 0번 정점
    ret = 0
    vnear = 0
    for _ in range(n - 1):
        # 현재까지 방문한 정점 집합에서 가장 가까운 정점을 찾는다.
        min = float('inf')
        for u in range(1, n):
            if 0 <= dist[u] < min:
                min = dist[u]
                vnear = u
        # 찾은 정점을 방문한다.
        ret += math.sqrt(dist[vnear])
        dist[vnear] = -1
        # 현재까지 방문한 정점 집합과의 거리를 업데이트한다.
        for u in range(1, n):
            if dist[u] > w[u][vnear]:
                dist[u] = w[u][vnear]
    return ret

for _ in range(int(input())):
    n, m = map(int, input().split()) # 건물의 수, 이미 설치된 케이블의 수
    x = list(map(int, input().split())) # 각 건물의 x 좌표
    y = list(map(int, input().split())) # 각 건물의 y 좌표
    w = [[0] * n for _ in range(n)] # 인접 행렬
    for u in range(n):
        for v in range(u, n):
            # 인접 행렬의 가중치: 연산 속도를 고려해 d^2으로 저장
            w[u][v] = w[v][u] = (x[u] -x[v])**2 + (y[u] - y[v])**2
    for _ in range(m):
        u, v = map(int, input().split())
        w[u][v] = w[v][u] = 0 # 이미 설치된 케이블의 가중치는 0으로 설정
    print(f"{lan(n,w):08f}")
