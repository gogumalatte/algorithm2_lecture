def maxsum(low, high):
    if low == high:
        return max(box[low], 0)
    else:
        mid = (low + high) // 2
        lmax = maxsum(low, mid)
        rmax = maxsum(mid+1, high)
        cmax = maxsum_crossing(low, mid, high)
        return max(lmax, rmax, cmax)
    
def maxsum_crossing(low, mid, high):
    left = float('-inf')
    curs = 0
    for i in range(mid, low - 1, -1):
        curs += box[i]
        left = max(left, curs)
    right = float('-inf')
    curs = 0
    for i in range(mid+1, high+1):
        curs += box[i]
        right = max(right, curs)
    return left + right
        
C = int(input())
for _ in range(C):
    N = int(input())
    box = list(map(int, input().split()))
    print(maxsum(0, N-1))
    
