import sys
cnt = int(sys.stdin.readline())
sum = 0
for _ in range(cnt):
    sum += int(sys.stdin.readline())

print(sum - cnt + 1)
