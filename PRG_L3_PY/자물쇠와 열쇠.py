def solution(key, lock):
    M, N = len(key), len(lock)
    x, y = [], []
    for i in range(N):
        for j in range(N):
            lock[i][j] = int(not lock[i][j])
            if lock[i][j]:
                y.append(i)
                x.append(j)
    
    if not x:
        return True

    a, b = [min(x), max(x)], [min(y), max(y)]
    s = [t[a[0]:a[1]+1] for t in lock[b[0]:b[1]+1]]
    m, n = len(s), len(s[0])

    r1 = [[0] * M for _ in range(M)]
    r2 = [[0] * M for _ in range(M)]
    r3 = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            r1[j][M-1-i] = key[i][j]
            r2[M-1-i][M-1-j] = key[i][j]
            r3[M-1-j][i] = key[i][j]

    for y in range(M-m+1):
        for x in range(M-n+1):
            for r in [key, r1, r2, r3]:
                if s == [t[x:x+n] for t in r[y:y+m]]:
                    return True
    return False
    
# 자물쇠를 subunit으로 자른 뒤 1과 0을 바꿈
# 매 key를 돌면서 있는지 찾음

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]],[[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
# print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
