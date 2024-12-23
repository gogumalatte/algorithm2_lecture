from heapq import heappush, heappop

MOD = 20090711
class RNG:
    def __init__(self, a, b):
        self.seed = 1983
        self.a = a
        self.b = b
    def next(self):
        ret = self.seed
        self.seed = ((self.seed * self.a) % MOD + self.b) % MOD
        return ret

def runningmedian(n, rnp):
    max_heap = []
    min_heap = []
    ret = 0
    for _ in range(n):
        if len(max_heap) == len(min_heap):
            heappush(max_heap, -rng.next())
        else:
            heappush(min_heap, rng.next())
        if min_heap and max_heap and min_heap[0] < -max_heap[0]:
            a = heappop(max_heap)
            b = heappop(min_heap)
            heappush(max_heap, -b)
            heappush(min_heap, -a)
        ret = (ret + (-max_heap[0])) % MOD
    return ret

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    rng = RNG(a, b) # 난수 생성기
    print(runningmedian(n, rng))
