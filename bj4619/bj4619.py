import sys
while True:
    b, n = map(int, sys.stdin.readline().split())
    if b == 0 and n == 0:
        break
    cur = 1
    under, upper = 0, 0
    while cur ** n < b:
        under = cur ** n
        cur += 1
        upper = cur ** n
    if b - under < upper - b:
        print(cur - 1)
    else:
        print(cur)
