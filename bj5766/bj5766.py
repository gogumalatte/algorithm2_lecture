'''
https://www.acmicpc.net/problem/5766
문제: 할아버지는 유명해!
난이도: 실버4
'''

while True:
    n, m = map(int, input().split())
    # 마지막 테스트 케이스
    if n == 0 and m == 0:
        break
    ranking = {}
    for _ in range(n):
        line = list(map(int, input().split()))
        for i in range(m):
            if line[i] not in ranking:
                ranking[line[i]] = 1
            else:
                ranking[line[i]] += 1
    sorted_rank = dict(sorted(ranking.items(), key=lambda item: (-item[1], item[0])))
    rank_value = list(sorted_rank.values())
    rank_keys = list(sorted_rank.keys())
    second_rank = rank_value[1]
    answer = []
    for i in range(1, len(rank_value)):
        if rank_value[i] != second_rank:
            break
        answer.append(rank_keys[i])
    print(' '.join(map(str, answer)))
