'''
P.2.2 게임판 덮기
H*W 크기의 게임판이 주어졌을 때, 남은 칸을 L자 모양의 블록으로 덮을 수 있는 방법의 수 찾기
(1) 완전 탐색으로 풀기
    게임판에서 흰 칸의 수가 3의 배수가 아닐 경우: 해답이 없다.
    이 외의 경우: 문제의 답을 생성하는 과정을 여러 조각으로 나눠 한 조각에 한 블록을 내려놓는다.
'''
from itertools import product

coverType = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)]
]

def boardcover(H, W, board):
    # 편의를 위해 board의 값을 0과 1로 바꾼다.
    board2 = [[0] * W for _ in range(H)]
    for i, j in product(range(H), range(W)):
        board2[i][j] = [0, 1][board[i][j] == '#']
    #흰 칸의 개수가 3의 배수가 아니면 모두 덮을 수 없다.
    if sum([row.count(0) for row in board2]) % 3 != 0:
        return 0
    else:
        return cover(H,W, board2)

def find_white(H, W, board):
    # 아직 채우지 못한 칸 중 가장 윗줄 가장 왼쪽에 있는 칸을 찾는다.
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def place(board, y, x, type, delta, H, W):
    # board의 (y, x)를 type 유형으로 처리한다.
    # delta가 1이면 덮고, -1이면 덮었던 블록을 제거한다.
    # 덮을 수 있으면 True, 덮을 수 있으면 False를 반환한다.
    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        if not ((0 <= ny < H) and (0 <= nx < W)): # 보드 밖으로 나간 경우
            ok = False
        else:
            board[ny][nx] += delta # 칸을 채우거나 제거한다.
            if (board[ny][nx] > 1): # 검은 칸이거나 겹쳐서 덮는 경우
                ok = False
    return ok

def cover(H, W, board):
    y, x = find_white(H, W, board) #비어 있는 첫 번째 칸을 찾는다.
    if y == -1:
        return 1 # 모든 칸을 채웠으므로 1을 반환한다.
    else:
        ret = 0
        for type in range(4): # 모든 블록 유형에 대해서 덮어본다.
            if (place(board, y, x, type, 1, H, W)):
                ret += cover(H, W, board) # 만약 덮을 수 있으면 재귀 호출한다.
            place(board, y, x, type, -1, H, W) # 덮은 블록을 제거한다.
        return ret

for _ in range(int(input())):
    H, W = map(int, input().split()) #게임판의 크기
    board = [input() for _ in range(H)] #게임판의 상태
    print(boardcover(H, W, board)) #흰 칸을 덮는 방법의 수
