'''
https://www.acmicpc.net/problem/15829 (Hashing)
'''

def char_to_num(char):
    return ord(char)-ord('a') + 1

r = 31
m = 1234567891

length = int(input())
words = input()
answer = 0

for i in range(0, length):
    num = char_to_num(words[i])
    answer += num * (r ** i)

answer = answer % m
print(answer)
