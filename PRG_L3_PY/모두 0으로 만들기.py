# def solution(a, edges):
#     if sum(a):
#         return -1
#     d = edges + [list(reversed(x)) for x in edges]
    
#     t = []
#     l = list(zip(*d))[0]
#     for x in d:
#         if l.count(x[0]) == 1:
#             t.append(x)
#     l = list(zip(*t))[1]
#     for x in t:
#         if l.count(x[1]) == 1:
#             t = x
#             break
        
#     edges.remove(sorted(t))
#     edges = [set(x) for x in edges]

#     b = [t[0],[t[1]]]
#     t = b
#     te = edges
#     while edges:
#         c = t[-1]
#         c.append([])
#         for e in edges:
#             if c[0] in e:
#                 c[-1].append((e-{c[0]}).pop())
#                 te.remove(e)
#         t = t[-1]
#         edges = [x for x in te]
    
#     f = 0
#     t = b
#     d = 0
#     while type(t[-1]) is list:
#         p = t
#         t = t[-1]
#         d += 1

#     while any(a):
#         t = p.pop()
#         v = 0
#         while t:
#             x = t.pop()
#             if a[x]:
#                 v += a[x]
#                 a[x] = 0
#         a[p[0]] += v
#         t = b
#         f += v
#         d -= 1
#         for i in range(d):
#             p = t
#             t = t[-1]
#     return f

# def solution(a, edges):
#     if sum(a):
#         return -1
#     N = len(a)
#     G = {x:set() for x in range(N)}
#     D = [list(a) for _ in range(N)]
#     for x,y in edges:
#         G[x].add(y)
#         G[y].add(x)
#     for o in range(N):
#         if a[o]:
#             D[o][o] = 0
#             s, v = [o], set()
#             while s:
#                 x = s.pop()
#                 v.add(x)
#                 s += G[x]-v
#                 for y in G[x]-v:
#                     D[o][x] += abs(D[o][y])
#                     D[o][y] = 0
#             if D[o].count(0) == N - 1:
#                 return sum(D[o])

def solution(a, edges):
    if sum(a):
        return -1
    N = len(a)
    G = {x:set() for x in range(N)}
    D = [list(a) for _ in range(N)]
    for x,y in edges:
        G[x].add(y)
        G[y].add(x)
    t = {x:len(G[x]) for x in G}
    m = max(t.values())
    O = [x for x in t if t[x] == m]
    for o in O:
        if a[o]:
            D[o][o] = 0
            s, v = [o], set()
            while s:
                x = s.pop()
                v.add(x)
                s += G[x]-v
                for y in G[x]-v:
                    D[o][x] += abs(D[o][y])
                    D[o][y] = 0
            if D[o].count(0) == N - 1:
                return sum(D[o])


print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))
print(solution([1,-1,0],[[0,1],[1,2]]))
print(solution([0,1,0],[[0,1],[1,2]]))