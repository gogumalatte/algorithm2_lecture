'''
https://www.acmicpc.net/problem/6376
문제: e 계산
난이도: 브론즈2
'''

print("n e")
print("- -----------")
print("0", "1")
i = 1
e = 1

for _ in range(1, 10):
    i = i * _
    e += 1 / i
 
    if _ == 1:
        print(_, int(e))
    elif _ <= 2:
        print(_, e)
    else:
        print(_, f"{e:.9f}")
