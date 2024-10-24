people = list(map(int, input().split()))
x, y, r = map(int, input().split())
crash = 0

for i in range(4):
    if people[i] == x:
        crash = i + 1

print(crash)
