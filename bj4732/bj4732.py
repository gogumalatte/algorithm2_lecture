'''
https://www.acmicpc.net/problem/4732
문제: 조옮김
난이도: 브론즈1
'''

while True:
    box = list(map(str, input().split()))
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    answer = []
    move = 0
    if box[0] == "***":
        break
    else:
        move = int(input())
    
    for i in box:
        cur = 0
        now = 0
        if i not in scale:
            if i[1] == 'b':
                for k in range(len(scale)):
                    if i[0] == scale[k]:
                        i = scale[k-1]
                        break
            elif i[1] == '#':
                for k in range(len(scale)):
                    if i[0] == scale[k]:
                        i = scale[k+1]
                        break
        for j in range(len(scale)):
            if i == scale[j]:
                cur = j
                break
        answer.append(scale[(cur + move) % 12])

    print(' '.join(map(str, answer)))
