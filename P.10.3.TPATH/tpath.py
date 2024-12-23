# Union-Find 클래스: Union-Find 자료구조를 이용하여 연결 상태를 관리하는 클래스
class UnionFind:
    def __init__(self, n):
        # 각 노드의 부모를 자기 자신으로 초기화
        self.parent = list(range(n))
        # 트리의 깊이를 저장하여 Union시 최적화
        self.rank = [0] * n
    
    def find(self, u):
        # 경로 압축 기법으로 루트 노드를 찾음
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        # 두 노드 u와 v를 연결
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # 랭크를 기준으로 트리 깊이를 최소화
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# 최소 경로 차이를 구하는 메인 함수
def tpath():
    global edges
    edges.sort(key=lambda x: x[2])  # 간선들을 가중치 순으로 정렬
    min_diff = float('inf')
    # 각 간선의 시작점을 i로 정하고 윈도우 슬라이딩을 사용
    for i in range(len(edges)):
        uf = UnionFind(n)  # 새로운 Union-Find 구조 초기화
        max_weight = -float('inf')
        
        # i번째 간선부터 MST를 형성하기 시작
        for j in range(i, len(edges)):
            a, b, w = edges[j]
            uf.union(a, b)  # 두 노드를 연결
            max_weight = w  # 현재 MST에서 가장 큰 가중치
            
            # 시작점(0)과 끝점(n-1)이 연결되었는지 확인
            if uf.find(0) == uf.find(n - 1):
                # 경로 가중치 차이의 최소값 업데이트
                min_diff = min(min_diff, max_weight - edges[i][2])
                break  # 현재 윈도우에서 가능한 최소 차이를 찾았으므로 종료
    
    return 0 if min_diff == float('inf') else min_diff

# 입력 및 결과 처리
INF = float('inf')
for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    ret = tpath()
    print(ret)
