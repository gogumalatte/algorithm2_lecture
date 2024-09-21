'''
https://www.acmicpc.net/problem/10816
'''
import sys

n = int(input())
n_box = sorted(list(map(int, input().split())))
hash_n_box = {}
m = int(input())
m_box = list(map(int, input().split()))
answer = []

for i in n_box:
    if i in hash_n_box:
        hash_n_box[i] += 1
    else:
        hash_n_box[i] = 1

for i in m_box:
    if i in hash_n_box:
        answer.append(hash_n_box[i])
    else:
        answer.append(0)

print(' '.join(map(str,answer)))
