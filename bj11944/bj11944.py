n, m = map(str,input().split())
answer = ""
# n을 반복했을 때 너무 긴 경우
if len(n) * int(n) > int(m):
    while len(answer) < int(m):
        answer = answer + n
    print(''.join(list(answer)[:int(m)]))
else:
    print(n*int(n))
