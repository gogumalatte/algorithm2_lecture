'''
https://www.acmicpc.net/problem/28702
'''

def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a = input()
b = input()
c = input()
answer = 0

if is_num(a):
    answer = int(a) + 3
elif is_num(b):
    answer = int(b) + 2
elif is_num(c):
    answer = int(c) + 1

if answer % 3 == 0 and answer % 5 == 0:
    print("FizzBuzz")
elif answer % 3 == 0 and answer % 5 != 0:
    print("Fizz")
elif answer % 3 != 0 and answer % 5 == 0:
    print("Buzz")
else:
    print(answer)
