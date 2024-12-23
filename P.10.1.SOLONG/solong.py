'''
P.10.1. 안녕히, 그리고 물고기는 고마웠어요! (ID: SOLONG)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = -1 # 이 노드에서 종료하는 문자열의 인덱스. 없으면 -1
        self.first = -1 # 이 노드를 루트로 하는 트라이에 가장 먼저 추가된 단어의 인덱스
    def find(self, key):
        if not key:
            return self
        else:
            char = key[0]
            if char not in self.children:
                return None
            return self.children[char].find(key[1:])

    def insert(self, key, id):
        if self.first == -1:
            self.first = id
        if not key:
            self.terminal = id
        else:
            char = key[0]
            if char not in self.children:
                self.children[char] = TrieNode()
            self.children[char].insert(key[1:], id)
    def type(self, key, id):
        if not key:
            return 0
        if self.first == id:
            return 1
        return 1 + self.children[key[0]].type(key[1:], id)

def count_keys(trie, word):
    node = trie.find(word)
    if not node or node.terminal == -1:
        return len(word)
    else:
        return trie.type(word, node.terminal)

def solong(dicwords, keywords):
    # 사전의 단어들을 출현 빈도의 내림차순, 단어의 오름차순으로 정렬한다.
    # 정렬된 순서로 추가하면 사전의 인덱스 번호를 각 노드의 추천 단어 번호로 쓸 수 있다.
    dicwords.sort(key=lambda x: (-int(x[1]), x[0]))
    trie = TrieNode()
    for i, x in enumerate(dicwords):
        trie.insert(x[0], i)
    trie.first = -1 # 아무 글자도 입력하지 않으면 자동완성을 하지 않는다.
    cnt = sum(count_keys(trie, s) for s in keywords)
    return cnt + len(keywords) - 1

for _ in range(int(input())):
    n, m = map(int, input().split()) # 사전에 포함된 단어의 수, 입력할 단어의 수
    dicwords = [input().split() for _ in range(n)] # 사전에 포함된 단어, 출현 빈도
    keywords = input().split() # 입력할 단어
    print(solong(dicwords, keywords))
