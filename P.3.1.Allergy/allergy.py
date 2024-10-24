def search(edible, chosen):
    global n, m, best, eaters, eatables
    if chosen >= best:
        return

    for friend, foods in eatables:  # 먹을 수 있는 음식이 적은 친구부터
        if edible[friend] == 0:  # 아직 먹을 음식이 없는 첫 번째 친구를 찾는다.
            break
    else:  # 모든 친구가 먹을 음식이 있는 경우
        best = chosen  # 최적해를 갱신하고
        return  # 종료

    for food in foods:  # 이 친구가 먹을 수 있는 음식을 하나 만든다.
        for j in eaters[food]:
            edible[j] += 1
        search(edible, chosen + 1)
        for j in eaters[food]:
            edible[j] -= 1

# 메인 코드 부분
for _ in range(int(input())):
    n, m = map(int, input().split())
    friends = {k: i for i, k in enumerate(input().split())}
    eaters = {i: [friends[name] for name in input().split()[1:]] for i in range(m)}
    eatables = {i:[]for i in range(n)}
    edible = [0] * n

    for k in eaters:
        for v in eaters[k]:
            eatables[v].append(k)

    # 먹을 수 있는 음식의 개수를 기준으로 오름차순 정렬
    eatables = sorted(eatables.items(), key=lambda x: len(x[1]))
    best = m + 1  # 답의 상한은 모든 음식을(+1)을 만드는 것이다.
    search([0] * n, 0)

    print(best)
