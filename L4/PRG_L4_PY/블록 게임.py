def solution(board):
    S = set(sum(board, [])) - {0}
    N = len(board)
    P = {x: set() for x in S}
    R = {x: set() for x in S}
    D = {x: 1 for x in S}
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                P[board[y][x]].add((x, y))
    for a in S:
        for x, y in P[a]:
            if (x, y-1) in P[a]:
                if (x-1, y-1) in P[a] or (x+1, y-1) in P[a]:
                    D[a] = 0
                    break
    for a in S:
        if D[a]:
            p, q = zip(*P[a])
            x1, x2, y1 = min(p), max(p), min(q)
            if x2 - x1 == 2:
                R[a] = {(x1, y1), (x1, y1+1), (x1+1, y1), (x1+1, y1+1), (x1+2, y1), (x1+2, y1+1)} - P[a]
            else:
                R[a] = {(x1, y1), (x1, y1+1), (x1, y1+2), (x1+1, y1), (x1+1, y1+1), (x1+1, y1+2)} - P[a]
    for i in range(len(S)):
        for a in S:
            for x, y in R[a]:
                for i in range(y+1):
                    if board[i][x]:
                        if not D[board[i][x]]:
                            D[a] = 0
                            break
    return sum(D.values())


# print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [
#       0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
# print(solution([[2, 2, 0, 0], [1, 2, 0, 4], [1, 2, 0, 4], [1, 1, 4, 4]]))
# print(solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [
#       1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [3, 0, 0, 2, 0],
    [3, 2, 2, 2, 0],
    [3, 3, 0, 0, 0]]))