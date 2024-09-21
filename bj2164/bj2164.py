'''
https://www.acmicpc.net/problem/2164
'''

from collections import deque

num = int(input())
deque_box = deque(list(range(1, num+1)))

while len(deque_box) > 1:
    deque_box.popleft()
    if len(deque_box) >= 2:
        deque_box.append(deque_box.popleft())

print(deque_box[0])
