'''
https://www.acmicpc.net/problem/2559
'''

n, k = map(int, input().split())
temps = list(map(int, input().split()))

window_sum = sum(temps[:k])
max_sum = window_sum

for i in range(1, n):
    if i < n - k + 1:
        window_sum = window_sum + temps[i+k-1] - temps[i-1]
        max_sum = max(max_sum, window_sum)

print(max_sum)
