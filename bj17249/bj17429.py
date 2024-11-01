string = list(map(str, input()))
is_face = False
left = 0
right = 0
for i in range(len(string)):
    if string[i] == '@' and not is_face:
        left += 1
    elif string[i] == '(':
        is_face = True
    elif string[i] == '@' and is_face:
        right += 1

print(left, right)