'''
decompress.py: 쿼드 트리 압축 해제
'''
def decompress(quadtree, y, x, size, decompressed):
    head = get_next(quadtree) # 문자열에서 다음 문자 가져오기
    if head in "bw": # 흰 색이거나 검은 색인 경우
        for i in range(y, y + size):
            decompressed[i][x:x+size] = [(head == "b")*1] * size
    else: # 재귀 호출
        half = size // 2
        decompress(quadtree, y, x, half, decompressed)
        decompress(quadtree, y, x + half, half, decompressed)
        decompress(quadtree, y + half, x, half, decompressed)
        decompress(quadtree, y + half, x + half, half, decompressed)

def get_next(quadtree):
    # static 변수를 이용하여 한 글자를 검사할 때마다 한 칸씩 앞으로 이동
    get_next.idx += 1
    return quadtree[get_next.idx - 1]

quadtree = "xxwwwbxwxwbbbwwxxxwwbbbwwwwbb"
size = 16 # 압축 해제 문제는 크기가 주어져야 함.
decompressed = [[0] * size for _ in range(size)]
get_next.idx = 0 # static 변수로 인덱스를 초기화
decompress(quadtree, 0, 0, 16, decompressed)
for i in range(len(decompressed)):
    print(*decompressed[i])