import sys

cnt = 0
while True:
    string = sys.stdin.readline().strip()
    if string == '':
        break
    cnt += 1

print(cnt)
