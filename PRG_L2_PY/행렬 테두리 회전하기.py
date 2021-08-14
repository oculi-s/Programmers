def solution(rows, columns, queries):
    m = [[columns*i+j+1 for j in range(columns)] for i in range(rows)]
    t = []
    for r1, c1, r2, c2 in queries:
        l = m[r1-1][c1-1:c2-1], m[r2-1][c1:c2]
        m = [list(x) for x in zip(*m)]
        t.append(min(min(*l[0],*l[1]), min(*m[c2-1][r1-1:r2-1], *m[c1-1][r1:r2])))
        m[c2-1][r1:r2], m[c1-1][r1-1:r2-1] = m[c2-1][r1-1:r2-1], m[c1-1][r1:r2]
        m = [list(x) for x in zip(*m)]
        m[r1-1][c1:c2], m[r2-1][c1-1:c2-1] = l
    return t


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# print(solution(3, 4, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# print(solution(2,2,[[1,1,2,2]]))
# print(solution(100,97, [[1,1,100,97]]))
