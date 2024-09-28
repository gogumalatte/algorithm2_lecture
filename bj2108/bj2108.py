'''
https://www.acmicpc.net/problem/2108
문제: 통계학
난이도: 실버3
'''
import sys

def myround(num):
    a = int(num)
    b = num - a
    if b >= 0.5:
        return a + 1
    elif b <= -0.5:
        return a - 1
    else:
        return a

index = int(input())
box = {}
for i in range(index):
    num = int(sys.stdin.readline())
    if num not in box:
        box[num] = 1
    else:
        box[num] += 1

sorted_by_key = dict(sorted(box.items(), key=lambda item: item[0])) # 숫자 크기 순으로 정렬
sorted_list = list(sorted_by_key.keys())

sorted_by_value = dict(sorted(box.items(), key=lambda item: (-item[1], item[0]))) # 빈도 순으로 정렬
freq_list = list(sorted_by_value.items())

# 산술평균 출력
sum = 0
for m, n in sorted_by_key.items():
    sum += m*n
print(myround(sum/index))

# 중간값 출력
n = 0
cur_index = 0
middle = 0
while cur_index <= int(index/2):
    middle = sorted_list[n]
    cur_index += sorted_by_key[middle]
    n+=1
print(middle)

# 최빈값 출력
if index == 1: # 요소가 하나 일때
    print(freq_list[0][0])
else:
    # 첫 번째 요소의 키와 값
    first_key, first_value = freq_list[0]
    # 두 번째 요소의 키와 값
    second_key, second_value = freq_list[1]
    if first_value == second_value:
        print(second_key)
    else:
        print(first_key)

# 범위
print(sorted_list[-1] - sorted_list[0])
