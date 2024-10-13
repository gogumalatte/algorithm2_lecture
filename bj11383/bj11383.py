'''
https://www.acmicpc.net/problem/11383
문제: 똚
난이도: 브론즈1
'''

n, m = map(int, input().split())
string1_box = []
string2_box = []
answer = "Eyfa"

for i in range(n):
    string1_box.append(input().strip())
for i in range(n):
    string2_box.append(input().strip())

for i in range(n):
    newString = []
    for j in range(m):
        newString.append(string1_box[i][j])
        newString.append(string1_box[i][j])
    if newString != list(string2_box[i]):
        answer = "Not Eyfa"

print(answer)
