# def solution(n, edge):
#     g = {x+1:[] for x in range(n)}
#     for x in edge:
#         g[x[0]].append(x[1])
#         g[x[1]].append(x[0])
    
#     d = {x+1:[] for x in range(n)}
#     s = [1]
#     v = []
#     while s:
#         n = s.pop()
#         if n not in v:
#             v.append(n)
#             s += set(g[n]) - set(v)
#             if not set(g[n]) - set(v):
#                 d[n].append(len(v))
#                 while not set(g[n]) - set(v):
#                     n = v.pop()
#                 v.append(n)
#             print(n,v,s)

#     print(d)
#     return True

def solution(n, edge):
    g = {x+1: set() for x in range(n)}
    for x in edge:
        g[x[0]].add(x[1])
        g[x[1]].add(x[0])

    s = [[1]]
    k = [0] * (n+1)
    while s:
        n = s.pop(0)
        a = g[n[-1]] - set(n)
        for x in a:
            if not k[x]:
                s.append(n+[x])
                k[x] = len(n)
        x = n[-1]
        k[x] = min(k[x], len(n))
    return sum(x == max(k) for x in k)


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
