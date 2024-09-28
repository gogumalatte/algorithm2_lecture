'''
https://www.acmicpc.net/problem/5341
문제: Pyramids
난이도: 브론즈5
'''

while True:
    num = int(input())
    if num == 0:
        break
    
    # Base가 짝수일 때, 1 ~ Base 까지의 합
    if num % 2 == 0:
        print((num//2) * (num + 1))
    # Base가 홀수일 때, 1 ~ Base 까지의 합
    else:
        print((num//2) * (num + 1) + (num//2 + 1))
