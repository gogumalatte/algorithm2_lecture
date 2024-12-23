def traversal(preorder, inorder):
    assert(len(preorder) == len(inorder))
    if preorder: # 텅 빈 트리면 곧장 종료
        root = preorder[0] # 전위 순회의 첫 원소는 루트 노드
        pos = inorder.index(root) # 중위 순회에서 루트 노드의 위치 (왼쪽 서브트리 크기)
        traversal(preorder[1:pos+1], inorder[:pos])
        traversal(preorder[pos+1:], inorder[pos+1:])
        print(root, end = " ")

for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    traversal(preorder, inorder)
    print()
