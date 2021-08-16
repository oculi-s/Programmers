def solution(n, path, order):
    g = {x:[] for x in range(n)}
    for x in path:
        g[x[0]].append(x[1])
        g[x[1]].append(x[0])
    s, v = [0], []
    while s:
        n = s.pop()
        if n not in v:
            v.append(n)
            s += set(g[n]) - set(v)
            
    print(v)
    return True

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))