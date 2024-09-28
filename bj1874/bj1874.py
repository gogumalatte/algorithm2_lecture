'''
https://www.acmicpc.net/problem/1874
문제: 스택 순열
난이도: 실버2
'''

import sys

def 백준1874():
    n = int(input())  # 입력 받을 숫자의 개수
    sequence = [int(sys.stdin.readline()) for _ in range(n)]  # 입력 수열
    
    stack = []  # 스택
    answer = []  # 출력할 결과 리스트
    current = 1  # 스택에 넣을 숫자
    possible = True  # 수열을 만들 수 있는지 여부
    
    for num in sequence:
        # 입력된 숫자보다 작거나 같은 숫자를 스택에 넣음
        while current <= num:
            stack.append(current)
            answer.append('+')
            current += 1
        
        # 스택의 마지막 숫자가 입력 숫자와 같으면 pop
        if stack and stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            possible = False
            break
    
    if possible:
        # 각 결과를 출력
        print('\n'.join(answer))
    else:
        print("NO")

백준1874()
