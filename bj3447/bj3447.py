'''
https://www.acmicpc.net/problem/3447
문제: 버그왕
'''
import sys

while True:
    source_code = sys.stdin.readline()
    # 마지막 소스코드가 끝나면 탈출
    if not source_code:
        break

    # 버그 제거
    while "BUG" in source_code:
        source_code = source_code.replace('BUG', '')
    sys.stdout.write(source_code)
