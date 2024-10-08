def festival(N, L, cost):
    psum = cost[:] + [0]
    print("psum:", psum)
    for i in range(N):
        psum[i] += psum[i-1]
    min_cost = float('inf')
    for i in range(N-L+1):
        for j in range(i + L - 1, N):
            avg_cost = (psum[j] - psum[i-1]) / (j - i + 1)
            min_cost = min(min_cost, avg_cost)
    return min_cost

C = int(input())
for _ in range(C):
    N, L = map(int, input().split())
    cost = list(map(int, input().split()))
    answer = festival(N, L, cost)
    print(answer)
