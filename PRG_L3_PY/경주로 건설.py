def solution(maps):
    N = len(maps)
    R = [[1, 1, 1, 0], [1, 0, 0, 1]]
    S = set(range(N))
    M = [N*1000]
    while R:
        v, d, y, x = R.pop(0)
        if [y, x] == [N-1, N-1]:
            M.append(v)
        elif v < min(M):
            for s in [d, 1-d]:
                for b, a in [[y+s, x+(1-s)], [y-s, x-(1-s)]]:
                    if {b, a} < S:
                        if not maps[b][a]:
                            if [v+1+5*(d != s), s, b, a] not in R:
                                R.append([v+1+5*(d != s), s, b, a])
    return 100*min(M)


def solution(maps):
    N = len(maps)
    R = [[1, 0, 1], [0, 1, 0]]
    V = [[[N*1000, N*1000] for _ in range(N)] for _ in range(N)]
    V[0][0], V[0][1], V[1][0] = [0, 0], [1, N*1000], [N*1000, 1]
    S = set(range(N))
    for y, x, d in R:
        for b, a in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
            if {b, a} < S:
                if not maps[b][a]:
                    n = a == x
                    c = d != n
                    v = V[y][x][d] + 1 + 5*c
                    if V[b][a][n] > v:
                        V[b][a][n] = v
                        R.append([b, a, n])
    for t in V:
        print(t)
    return min(V[N-1][N-1]) * 100

def solution(maps):
    N = len(maps)
    M = N**2*5+1
    V = [[[M, M] for _ in range(N+1)] for _ in range(N+1)]
    V[0][0] = [0, 0]
    for _ in range(N**2):
        for y in range(N):
            for x in range(N):
                if not maps[y][x]:
                    V[y][x][0] = min(V[y][x][0], V[y][x+1][0]+1, V[y][x-1][0]+1, V[y-1][x][1]+6, V[y+1][x][1]+6)
                    V[y][x][1] = min(V[y][x][1], V[y][x+1][0]+6, V[y][x-1][0]+6, V[y-1][x][1]+1, V[y+1][x][1]+1)
    return min(V[N-1][N-1]) * 100

print(solution(	[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]),3200)
print(solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]), 2100)
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),900)
# print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]),3000)
