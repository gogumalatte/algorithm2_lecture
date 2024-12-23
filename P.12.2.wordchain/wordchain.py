from collections import defaultdict
to_index = lambda word: (ord(word[0]) - ord('a'), ord(word[-1]) - ord('a'))

def make_graph(words):
    adj = [[0] * 26 for _ in range(26)]
    graph = defaultdict(list)
    indeg = [0] * 26
    outdeg = [0] * 26
    for i in range(len(words)):
        a, b = to_index(words[i])
        graph[(a,b)].append(words[i])
        adj[a][b] += 1
        outdeg[a] += 1
        indeg[b] += 1
    return adj, graph, indeg, outdeg

def checkEuler(indeg, outdeg):
    plus1, minus1 = 0, 0
    for i in range(26):
        delta = outdeg[i] - indeg[i]
        if delta < -1 or 1 < delta:
            return False
        if delta == 1:
            plus1 += 1
        if delta == -1:
            minus1 += 1
    return (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0)

def getEulerCircuit(here, circuit, adj):
    for there in range(len(adj)):
        while adj[here][there] > 0:
            adj[here][there] -= 1
            getEulerCircuit(there, circuit, adj)
    circuit.append(here)

def getEulerTrailOrCircuit(adj, indeg, outdeg):
    circuit = []
    for i in range(26):
        if outdeg[i] == indeg[i] + 1:
            getEulerCircuit(i, circuit, adj)
            return circuit
    for i in range(26):
        if outdeg[i] != 0:
            getEulerCircuit(i, circuit, adj)
            return circuit
    return circuit

def wordchain(words):
    adj, graph, indeg, outdeg = make_graph(words)
    if not checkEuler(indeg, outdeg):
        return "IMPOSSIBLE"
    circuit = getEulerTrailOrCircuit(adj, indeg, outdeg)
    if len(circuit) != len(words) + 1:
        return "IMPOSSIBLE"
    circuit.reverse()
    ret = ""
    for i in range(1, len(circuit)):
        a, b = circuit[i-1], circuit[i]
        if len(ret) != 0:
            ret += " "
        ret += graph[(a, b)][-1]
        graph[(a, b)].pop()
    return ret

for _ in range(int(input())):
    n = int(input())
    words = [input() for _ in range(n)]
    print(wordchain(words))