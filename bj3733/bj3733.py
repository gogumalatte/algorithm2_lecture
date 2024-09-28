'''
https://www.acmicpc.net/problem/3733
문제: Shares
난이도: 브론즈5
'''

import sys

input_all = sys.stdin.read()

input_box = input_all.split()

for i in range(0, len(input_box), 2):
    m = int(input_box[i])
    n = int(input_box[i+1])
    
    max_shares = n // (m + 1)
    print(max_shares)
