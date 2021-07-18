# def solution(n, costs):
#     v = [[0]*n for _ in range(n)]
#     g = {x: set() for x in range(n)}
#     for x, y, z in costs:
#         v[x][y] = z
#         v[y][x] = z
#         g[x].add(y)
#         g[y].add(x)
#     d = []
#     k = 0
#     for x in g:
#         if len(g[x]) == 1:
#             f = g[x].pop()
#             k += v[x][f]
#             g[f] -= {x}
#     g = {a:b for a,b in g.items() if b}
#     for i in g.keys():
#         a = [[[i], k]]
#         while a:
#             b, c = a.pop()
#             if set(b) == set(g.keys()):
#                 d.append(c)
#             else:
#                 for x in g[b[-1]]:
#                     if x not in b:
#                         t = b + [x]
#                         a.append([t, c + v[b[-1]][x]])
#     return min(d or [k])

def solution(n,costs):
    V = [[0]*n for _ in range(n)]
    G = {x:set() for x in range(n)}
    for x,y,z in costs:
        V[x][y], V[y][x] = z, z
        G[x].add(y), G[y].add(x)

    for o in range(n):
        R = [[o,[0]]]
        M = []
        while R:
            print(R,M)
            v, r = R.pop(0)
            x = r[-1]
            for y in G[x] - set(r):
                if len(r+[y]) == n:
                    M.append(v+V[x][y])
                else:
                    R.append([v+V[x][y],r+[y]])
    return min(M)

# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
# print(solution(5,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]),15) #15
# print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] ),8) #8
# print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] ),9) #9
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] ),104) #104
print(solution(6,[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]),11) #11
print(solution(5,[[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]]),8) #8
print(solution(5,[[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]),8) #8
print(solution(5,[[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]),6) #6
print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]),15) #15
print(solution(5,[[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]))
