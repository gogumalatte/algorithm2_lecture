'''
https://www.acmicpc.net/problem/4564
문제: 숫자 카드놀이
난이도: 브론즈2
'''

while True:
    num = input()
    box = []
    index = 0
    if num == "0" :
        break
    
    box.append(num)
    while box[-1] != "0":
        if len(box[index]) == 1:
            break
        mult = 1
        for i in range(len(box[index])):
            mult = mult * int(box[index][i])
        box.append(str(mult))
        index += 1
    print(' '.join(box))
