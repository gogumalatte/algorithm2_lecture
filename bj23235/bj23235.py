current = 1
while True:
    mylist = list(map(int, input().split()))
    if len(mylist) == 1 and mylist[0] == 0:
        break
    print(f'Case {current}: Sorting... done!')
    current += 1
