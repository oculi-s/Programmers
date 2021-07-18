def solution(m, n, puddles):
    b = [[0]*(m+2)]+[[0]+[1]*m+[0] for _ in range(n)]+[[0]*(m+2)]
    for x, y in puddles:
        b[y][x] = 0
    r = [(1, 1)]
    s = [r]
    v = 0
    while s:
        r = s.pop(0)
        x, y = r[-1]
        if (x, y) == (m, n):
            v += 1
        else:
            if b[y+1][x] and (x, y+1) not in r:
                s.append(r + [(x, y+1)])
            if b[y][x+1] and (x+1, y) not in r:
                s.append(r + [(x+1, y)])
    return v % 1000000007

def solution(m, n, puddles):
    v = [[0]*(m+2) for _ in range(n+2)]
    v[1][0] = 1
    for y in range(n):
        for x in range(m):
            if [x+1, y+1] not in puddles:
                v[y+1][x+1] = v[y][x+1] + v[y+1][x]
    return v[n][m] % 1000000007

# print(solution(1, 2, []))
print(solution(4, 3, [[2, 2]]))
