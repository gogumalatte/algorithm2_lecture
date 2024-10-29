'''
P.3.2. 울타리 잘라내기 (ID. FENCE): 분할정복 알고리즘
'''
def fence(h, left, right):
    if left == right:
        return h[left]
    else:
        mid = (left + right) // 2
        # 왼쪽[left, mid]과 오른쪽[mid+1, right] 부분 문제를 각개 격파
        ret = max(fence(h, left, mid), fence(h, mid + 1, right))
        # 두 부분에 모두 걸치는 경우의 가장 큰 사각형 고려
        return max(ret, largest_in_between(h, left, mid, right))

def largest_in_between(h, left, mid, right):
    low, high = mid, mid + 1 # 경계에 있는 두 판자
    height = min(h[low], h[high]) # 중에서 더 작은 것을 선택
    ret = height * 2 # 두 판자에서 잘라낸 사각형의 넓이
    while left < low or right > high: # 사각형이 입력 전체를 덮을 때까지
        if high < right and (low == left or h[low - 1] < h[high + 1]):
            high += 1 # 오른쪽으로 한 칸 확장
            height = min(height, h[high])
        else:
            low -= 1 # 왼쪽으로 한 칸 확장
            height = min(height, h[low])
        ret = max(ret, height * (high - low + 1)) # 확장 후 사각형의 넓이 업데이트
    return ret

for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    print(fence(h, 0, n - 1))
