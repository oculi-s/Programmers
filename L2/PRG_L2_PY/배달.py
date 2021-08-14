# def solution(N, road, K):
#     g = [[2001]*(N+1) for _ in range(N+1)]
#     for x in road:
#         g[x[0]][x[1]] = min(x[2],g[x[0]][x[1]])
#         g[x[1]][x[0]] = min(x[2],g[x[1]][x[0]])
#     a = 0
#     r = 1
#     v = 0
#     while g[r][x] < 2000:
#         r = x
#         for x in range(1,N+1):
#             v += g[r][x]
#             if v > K:
#                 print(r,x)
#                 a += 1
#                 break
#     return a

# def solution(N, road, K):
#     v = [[0]*N for _ in range(N)]
#     g = {x: set() for x in range(N)}
#     k = [0]*N
#     for x, y, z in road:
#         x, y = x-1, y-1
#         if not v[x][y] or z < v[x][y]:
#             v[x][y] = z
#         if not v[y][x] or z < v[y][x]:
#             v[y][x] = z
#         g[y].add(x)
#         g[x].add(y)
#     s, t = [0], []
#     while s:
#         n = s.pop(0)
#         if n not in t:
#             t.append(n)
#             a = g[n] - set(t)
#             c = set()
#             for x in a:
#                 b = v[n][x] + k[n]
#                 if not k[x] or b < k[x]:
#                     k[x] = b
#                 else:
#                     c.add(x)
#             s += a - c
#     return sum(x <= K for x in k)

def solution(N, road, K):
    v = [[0]*N for _ in range(N)]
    for x, y, z in road:
        x, y = x-1, y-1
        if not v[x][y] or z < v[x][y]:
            v[x][y] = z
            v[y][x] = z
    for _ in range(N):
        for x in range(N):
            for y in range(N):
                if v[y][x] and v[0][y]:
                    if not v[0][x] or v[0][y] + v[y][x] < v[0][x]:
                        v[0][x] = v[0][y] + v[y][x]
    v[0][0] = 0
    return sum(x <= K for x in v[0])


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
      [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3), 4)
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
      3, 4, 3], [3, 5, 3], [3, 5, 2], [5, 6, 1]], 4), 4)
