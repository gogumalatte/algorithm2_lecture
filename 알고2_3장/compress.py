'''
compress.py: 쿼드 트리 압축하기
'''
def compress(quadtree, y, x, size):
    ret = check(quadtree, y, x, size)
    if ret != "x": # 모두 흰 색이건나 검은 색이면
        return ret # 해당 색을 반환하고 종료
    else:
        half = size // 2 # 크기를 절반으로 자른다.
        qt1 = compress(quadtree, y, x, half) # 1. 상단 왼쪽 조각
        qt2 = compress(quadtree, y, x + half, half) # 2. 상단 오른쪽 조각
        qt3 = compress(quadtree, y + half, x, half) # 3. 하단 왼쪽 조각
        qt4 = compress(quadtree, y + half, x + half, half) # 4. 하단 오른쪽 조각
        return "x" + qt1 + qt2 + qt3 + qt4

def check(quadtree, y, x, size):
    # 주어진 시작 좌표(y, x)와 크기 (size) 범위에서
    # 모두 흰 색(합이 0)이거나 모두 검은 색(합이 size * size)인가를 확인
    s = sum([sum(quadtree[i][x:x+size]) for i in range(y, y + size)])
    return "w" if s == 0 else "b" if s == size * size else "x"

# 쿼드 트리 데이터 정의
quadtree = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 쿼드 트리 압축 수행 함수 호출
print(compress(quadtree, 0, 0, len(quadtree)))
