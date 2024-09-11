from itertools import product

# 블록 모양들 (회전된 모든 경우의 수)
coverType = [
    [(0, 0), (1, 0), (0, 1)],  # ┌─
    [(0, 0), (0, 1), (1, 1)],  # ─┘
    [(0, 0), (1, 0), (1, 1)],  # └─
    [(0, 0), (1, 0), (1, -1)]  # ─┐
]

def boardcover(H, W, board):
    # 보드를 숫자 형태로 변환 (# -> 1, . -> 0)
    board2 = [[0] * W for _ in range(H)]
    for i, j in product(range(H), range(W)):
        board2[i][j] = [0, 1][board[i][j] == '#']
    
    # 빈 칸이 3의 배수가 아니면 불가능
    if sum([row.count(0) for row in board2]) % 3 != 0:
        return 0
    else:
        return cover(H, W, board2)

def find_white(H, W, board):
    # 빈 칸(0)을 찾음
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                return i, j
    return -1, -1    

def place(board, y, x, cover_type, delta, H, W):
    # 블록을 놓거나 되돌리는 함수 (delta가 1이면 놓고, -1이면 되돌림)
    ok = True
    for i in range(3):
        ny = y + coverType[cover_type][i][0]
        nx = x + coverType[cover_type][i][1]
        if not (0 <= ny < H and 0 <= nx < W):
            ok = False
        else:
            board[ny][nx] += delta
            if board[ny][nx] > 1:  # 겹치면 안됨
                ok = False
    return ok

def cover(H, W, board):
    # 보드에서 빈 칸을 찾음
    y, x = find_white(H, W, board)
    
    # 빈 칸이 없으면 (기저 사례)
    if y == -1:
        return 1
    else:
        ret = 0
        for cover_type in range(4):
            if place(board, y, x, cover_type, 1, H, W):
                ret += cover(H, W, board)
            place(board, y, x, cover_type, -1, H, W)  # 되돌리기
    return ret

# 입력 처리
for _ in range(int(input())):
    H, W = map(int, input().split())
    board = [input() for _ in range(H)]
    print(boardcover(H, W, board))
