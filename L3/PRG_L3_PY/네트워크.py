def solution(n, computers):
    g = {x+1:set() for x in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j]:
                    g[i+1].add(j+1)
    v = set()
    a = set(range(1,n+1))
    t = 0
    while a:
        s = [a.pop()]
        while s:
            n = s.pop()
            if n not in v:
                v.add(n)
                s += g[n] - v
        t += 1
        a -= v
    return t

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))