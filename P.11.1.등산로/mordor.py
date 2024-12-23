import sys

class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr  # 입력 배열 저장
        self.nodes = [0] * (4 * n)
        self.init(1, 0, n - 1)
    
    def init(self, node, left, right):
        if left == right:
            self.nodes[node] = self.arr[left]
            return self.nodes[node]
        else:
            mid = (left + right) // 2
            lmin = self.init(node * 2, left, mid)
            rmin = self.init(node * 2 + 1, mid + 1, right)
            self.nodes[node] = min(lmin, rmin)
            return self.nodes[node]
    
    def query(self, node, low, high, left, right):
        if right < low or high < left:
            return float('inf')
        elif left <= low and high <= right:
            return self.nodes[node]
        else:
            mid = (low + high) // 2
            lmin = self.query(node * 2, low, mid, left, right)
            rmin = self.query(node * 2 + 1, mid + 1, high, left, right)
            return min(lmin, rmin)

def mordor(n, h, queries):
    # 최소값 세그먼트 트리
    min_tree = SegmentTree(n, h)
    # 최대값 세그먼트 트리 (음수로 저장 후 결과의 부호 반전)
    max_tree = SegmentTree(n, [-x for x in h])
    
    # 쿼리 처리
    for a, b in queries:
        range_min = min_tree.query(1, 0, n - 1, a, b)
        range_max = max_tree.query(1, 0, n - 1, a, b)
        print(-range_max - range_min)

# 입력 처리
input = sys.stdin.readline
for _ in range(int(input().strip())):
    n, q = map(int, input().split())
    h = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]
    mordor(n, h, queries)
