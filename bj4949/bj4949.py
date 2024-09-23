'''
https://www.acmicpc.net/problem/4949
'''


while (True):
    line = input()
    if line == ".":
        break
    
    box = []
    is_balanced = True
    
    for char in line:
        if char == '(' or char == '[':
            box.append(char)
        elif char == ')':
            if len(box) == 0 or box[-1] != '(':
                is_balanced = False
                break
            box.pop()
        elif char == ']':
            if len(box) == 0 or box[-1] != '[':
                is_balanced = False
                break
            box.pop()
    
    if is_balanced == True and len(box) == 0:
        print("yes")
    else:
        print("no")

