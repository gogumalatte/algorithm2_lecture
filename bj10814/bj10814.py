'''
https://www.acmicpc.net/problem/10814
나이순 정렬
'''

index = int(input())

box = []

for _ in range(index):
    age, name = map(str, input().split())
    box.append([int(age), name, _])
    
sorted_box = sorted(box, key = lambda x : (x[0], x[2]))

for i in range(index):
    print(sorted_box[i][0], sorted_box[i][1])
