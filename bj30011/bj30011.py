'''
https://www.acmicpc.net/problem/30011
문제: 겹다각형의 각
난이도: 실버4
'''
n = int(input())
angle_list = list(map(int, input().split()))
answer = 0
for i in range(n):
    if i == 0: #제일 바깥 도형의 경우
        answer += 180 * (angle_list[i] - 2)
    else:
        answer += 180 * angle_list[i]
print(answer)
