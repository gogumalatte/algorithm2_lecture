'''
https://www.acmicpc.net/problem/2775
'''

def people(k, n):
    floor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for _ in range(k):
        for i in range(1, n):
            floor[i] = floor[i] + floor[i-1]
    print(floor[n-1])

case = int(input())
for _ in range(case):
    k = int(input())
    n = int(input())
    people(k, n)
    