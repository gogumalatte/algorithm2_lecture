import sys
input = sys.stdin.readline
TIME_SIZE = 1000000  # 상수 이름 통일

class FenwichTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def add(self, pos, x):
        pos += 1
        while pos < len(self.tree):  # 수정: pos가 tree 길이보다 작을 때까지 반복
            self.tree[pos] += x
            pos += (pos & -pos)
    
    def sum(self, pos):
        pos += 1
        ret = 0
        while pos > 0:
            ret += self.tree[pos]
            pos &= pos - 1
        return ret

def measuretime(n, A):
    tree = FenwichTree(TIME_SIZE)
    ret = 0
    for i in range(n):
        ret += tree.sum(TIME_SIZE - 1) - tree.sum(A[i])
        tree.add(A[i], 1)
    return ret

for _ in range(int(input().strip())):
    n = int(input().strip())
    A = list(map(int, input().split()))
    
    # 입력 값이 TIME_SIZE 범위를 벗어나는 경우 대비
    if max(A) >= TIME_SIZE or min(A) < 0:
        print("Error: Input values out of range.")
        continue

    print(measuretime(n, A))
