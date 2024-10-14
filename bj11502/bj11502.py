'''
https://www.acmicpc.net/problem/11502
문제: 세 개의 소수 문제
난이도: 실버4
'''

def is_prime(num):
    temp = 0
    for i in range(1, num+1):
        if num % i == 0:
            temp += 1
    if temp == 2:
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    k = int(input())
    prime_box = []
    answer = []
    found = False
    for i in range(2, k):
        if is_prime(i):
            prime_box.append(i)
    
    for first in range(len(prime_box)):
        for second in range(first, len(prime_box)):
            for third in range(second, len(prime_box)):
                sum = prime_box[first] + prime_box[second] + prime_box[third]
                if k == sum:
                    answer = [prime_box[first], prime_box[second], prime_box[third]]
                    found = True
                    break
            if found == True:
                break
        if found == True:
            break
    if found == True:
        print(*answer)
    else:
        print(0)
