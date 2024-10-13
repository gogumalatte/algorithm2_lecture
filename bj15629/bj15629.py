'''
https://www.acmicpc.net/problem/15629
문제: Africa
난이도: 브론즈1
'''
import sys

n = int(input())
countries = []
biza = 0
for _ in range(n):
    countries.append(sys.stdin.readline().strip())

for i in range(n):
    match countries[i]:
        case 'ethiopia':
            biza += 50
        case 'kenya':
            biza += 50
        case 'namibia':
            biza += 140
        case 'tanzania':
            biza += 50
        case 'zambia':
            biza += 50
        case 'zimbabwe':
            biza += 30
    
    if countries[i] == 'south-africa':
        if 'namibia' in countries[i:]:
            biza -= 100

    if i != n - 1:
        if countries[i] == "zambia" and countries[i + 1] == "zimbabwe":
            biza -= 30
        if countries[i] == "zimbabwe" and countries[i + 1] == "zambia":
            biza -= 30

print(biza)
