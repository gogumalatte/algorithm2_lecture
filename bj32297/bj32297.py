'''
https://www.acmicpc.net/problem/32297
문제: 문자열을 만들어요
난이도: 브론즈3
'''

index = int(input())
string = input()

g_index = []
answer = False

for i in range(index):
    if string[i] == 'g' and i <= 6:
        g_index.append(i)

for i in g_index:
    if string[i + 1] == 'o' and string[i + 2] == 'r' and string[i + 3] == 'i':
        answer = True

if answer == True:
    print("YES")
else:
    print("NO")
