r, c, zr, zc = map(int, input().split())
box = []
for _ in range(r):
    box.append(input())

for i in range(r):
    for _ in range(zr):
        for j in range(c):
            print(box[i][j]*zc, end='')
        print()
