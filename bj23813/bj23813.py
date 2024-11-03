num = int(input())
len_num = len(str(num))
sum = 0

for i in range(len_num):
    last_digit = num % 10  # 맨 뒤의 자릿수를 구함
    num = num // 10  # 마지막 자릿수를 제외한 숫자로 만듦
    num = last_digit * (10 ** (len_num - 1)) + num  # 회전된 숫자 생성
    sum += num  # 회전된 숫자를 더함

print(sum)