def solution(n, edges):
    G = {x: set() for x in range(n)}
    for x, y in edges:
        G[x-1].add(y-1)
        G[y-1].add(x-1)
    M = [[0]*n for _ in range(n)]
    for o in range(n):
        s, v = [o], set()
        for x in s:
            v.add(x)
            s += G[x] - v
            for t in G[x] - v:
                if t > o:
                    M[o][t] = M[o][x] + 1
    return sorted(sum(M,[]))[-2]

from itertools import combinations
def solution(n, edges):
    n += 1
    V = [[n**2]*n for _ in range(n)]
    for x, y in edges:
        V[x][y], V[y][x] = 1, 1
    for i in range(1,n):
        for j in range(1,n):
            if i != j:
                for k in range(1,n):
                    V[i][j] = min(V[i][j],V[i][k]+V[k][j])
        V[i] = [0 if x==n**2 else x for x in V[i]]
    A = []
    for x,y,z in combinations(range(1,n),3):
        A.append(sorted([V[x][y],V[y][z],V[z][x]])[-2])
    return max(A)

print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]))
