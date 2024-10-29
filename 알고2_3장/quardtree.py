'''
P.3.1. 쿼드 트리 뒤집기
압축을 풀지 않고도 쿼드 트리를 뒤집을 방법이 필요하다.
종료 조건: 전체가 한 가지 색(b,w)일 경우 뒤집을 필요가 없다. 그대로 반환
재귀 조건: 두 가지 색이 섞여 있을 경우(x), 네 부분으로 쪼개어 각각을 상하로 뒤집은 다음 이들을 상하로 뒤집히도록 병합하여 반환한다.
'''
def quadtree_reverse(quadtree):
    head = get_next(quadtree)
    if head in "bw": # 한 가지 색일 경우
        return head # 그 색을 반한
    else:
        # 네 부분으로 4분할하여 각각을 뒤집는다.
        qt1 = quadtree_reverse(quadtree)
        qt2 = quadtree_reverse(quadtree)
        qt3 = quadtree_reverse(quadtree)
        qt4 = quadtree_reverse(quadtree)
        return "x" + qt3 + qt4 + qt1 + qt2

# 정적 변수를 이용하여 quadtree에서 한 문자씩 꺼내어 반환
def get_next(quadtree):
    get_next.idx += 1 # 인덱스를 다음 위치로
    return quadtree[get_next.idx - 1] # 이전 인덱스 값을 리턴

for i in range(int(input())):
    quadtree = input()
    get_next.idx = 0 # 정적 변수로 인덱스를 초기화
    reversed = quadtree_reverse(quadtree)
    print(reversed)
