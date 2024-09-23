'''
https://www.acmicpc.net/problem/11866
'''

n, k = map(int, input().split())

box = list(range(1, n+1))
answer = []
current = 0

while len(box) >= 1 :
    current = (current + (k-1)) % n
    answer.append(box.pop(current))
    n -= 1

formatted_output = "<" + ", ".join(map(str, answer)) + ">"
print(formatted_output)
