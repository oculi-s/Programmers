# def solution(n, s, a, b, fares):
#     s, a, b = s-1, a-1, b-1
#     f = [[0] * n for _ in range(n)]
#     g = {x: set() for x in range(n)}
#     for x, y, z in fares:
#         x, y = x-1, y-1
#         f[x][y], f[y][x] = z, z
#         g[x].add(y)
#         g[y].add(x)
#     C, D = [[s], [a], [b]], []
#     for c in C:
#         v, o, d = set(), c[0], [0]*n
#         for p in c:
#             if p not in v:
#                 v.add(p)
#                 for x in g[p] - {o}:
#                     if not d[x] or d[x] > f[p][x]+d[p]:
#                         d[x] = f[p][x]+d[p]
#                 c += g[p] - v - {o}
#         D.append(d)
#     return min(sum(x) for x in zip(*D) if sum(x))

def solution(n, s, a, b, fares):
    f = [[0] * n for _ in range(n)]
    for x, y, z in fares:
        f[x-1][y-1], f[y-1][x-1] = z, z
    for i in range(n):
        for j in range(n):
            if i != j and not f[i][j]:
                for k in range(n):
                    if k != i and k != j:
                        if f[j][k] and f[i][k] and (not f[i][j] or f[j][k] + f[i][k] < f[i][j]):
                            f[i][j] = f[j][k] + f[i][k]
            f[i][j] = f[i][j] or f[j][i]
            f[j][i] = f[i][j] or f[j][i]
    return min(sum(x) for x in zip(f[s-1],f[a-1],f[b-1]) if sum(x))

def solution(n, s, a, b, fares):
    V = [[0] * (n+1) for _ in range(n+1)]
    G = {x: set() for x in range(n+1)}
    for x, y, z in fares:
        V[x][y], V[y][x] = z, z
        G[x].add(y)
        G[y].add(x)
    D = []
    for o in [s, a, b]:
        s, v, T = [o], set(), [0]*(n+1)
        for x in s:
            v.add(x)
            for y in G[x]-{o}:
                if not T[y] or T[y] > V[x][y]+T[x]:
                    T[y] = V[x][y]+T[x]
            s += G[x]-v-{o}
        D.append(T)
    return min(sum(x) for x in zip(*D) if sum(x))

def solution(n, s, a, b, fares):
    M = 100000*200
    n += 1
    V = [[M] * n for _ in range(n)]
    for x, y, z in fares:
        V[x][y], V[y][x] = z, z
    for i in [s,a,b]:
        for _ in range(int(n**.5)):
            for j in range(1,n):
                if i != j:
                    for k in range(1,n):
                        V[i][j] = min(V[i][j],V[i][k]+V[k][j])
        for j in range(n):
            if V[i][j] == M:
                V[i][j] = 0
    S = [sum(x) for x in zip(V[s],V[a],V[b])]
    return min(S[1:])

print(solution(	6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(	7, 3, 4, 1, [[5, 7, 9], [
    4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(	6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [
      6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
