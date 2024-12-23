import math
red, brown = map(int, input().split())
a, b = 0, 0
for i in range(1, int(math.sqrt(brown)) + 1):
    if brown % i == 0 and (i + 2) * (brown // i + 2) == red + brown:
        a = i + 2
        b = (brown // i + 2)
        break

if a > b:
    print(a, b)
else:
    print(b, a)
