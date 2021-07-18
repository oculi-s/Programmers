# def solution(board, r, c):
#     R = [[0, board[r][c], [r, c], board]]
#     S = set(range(4))
#     V = [[0]*4 for _ in range(4)]
#     board[r][c], V[r][c] = 0, 1

#     while R:
#         v, e, [y, x], board = R.pop(0)
#         if not any(sum(board, [])):
#             return v

#         L = set()
#         D = [[[x+1,y],[x+2,y],[x+3,y]],[[x-1,y],[x-2,y],[x-3,y]],[[x,y+1],[x,y+2],[x,y+3]],[[x,y-1],[x,y-2],[x,y-3]]]
#         for t in D:
#             for a,b in t:
#                 if {a,b} < S:
#                     if board[b][a]:
#                         L.add((a,b))
#                         break
#         for a,b in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
#             if {a,b} < S:
#                 L.add((a,b))
#         for a, b in L:
#             if e:
#                 # 가진게 새로운 것과 동일
#                 if e == board[b][a]:
#                     B = [list(t) for t in board]
#                     B[b][a] = 0
#                     R.append([v+2, 0, [b, a], B])
#                     V = [[0]*4 for _ in range(4)]
#                 # 가진게 있는데 그냥 이동
#                 elif not V[b][a]:
#                     V[b][a] = 1
#                     R.append([v+1, e, [b, a], board])
#             else:
#                 # 가진게 없는데 새로 발견
#                 if board[b][a]:
#                     B = [list(t) for t in board]
#                     e, B[b][a] = B[b][a], 0
#                     R.append([v+2, e, [b, a], B])
#                     V = [[0]*4 for _ in range(4)]
#                 # 가진게 없이 그냥 이동
#                 elif not V[b][a]:
#                     V[b][a] = 1
#                     R.append([v+1, e, [b, a], board])
#         for t in board:
#     print(t)
# print()
# print(a,b,x,y)

def solution(board, r, c):
    D = list(range(max(sum(board,[]))+1))
    S = set(range(4))
    V = [[0]*4 for _ in range(4)]
    O = [[0]*4 for _ in range(4)]
    V[r][c] = 1
    R = [[0, board[r][c], [r, c], D, V]]
    board[r][c] = 0

    while R:
        v, e, [y, x], D, V = R.pop(0)
        print(v,e,x,y,D)
        if not D:
            return v

        L = set()
        for i in range(1, 4):
            if x+i < 4:
                if board[y][x+i]:
                    L.add((x+i, y))
                    break
        for i in range(1, 4):
            if x-i >= 0:
                if board[y][x-i]:
                    L.add((x-i, y))
                    break
        for i in range(1, 4):
            if y-i >= 0:
                if board[y-i][x]:
                    L.add((x, y-i))
                    break
        for i in range(1, 4):
            if y+i < 4:
                if board[y+i][x]:
                    L.add((x, y+i))
                    break

        for a, b in L | {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}:
            if {a, b} < S:
                if not D[board[b][a]] or (e and e != board[b][a]):
                    if not V[b][a]:
                        V[b][a] = 1
                        R.append([v+1, e, [b, a], D, V])
                elif not e or (D[e] and e == board[b][a]):
                    T = None
                    if e == board[b][a]:
                        T = list(D)
                        T[board[b][a]] = 0
                    e = (not e) * board[b][a]
                    R.append([v+2, e, [b, a], T or D, [list(t) for t in O]])

# def solution(board, r, c):
#     R = [[0, board[r][c], [r, c], board]]
#     S = set(range(4))
#     V = [[0]*4 for _ in range(4)]
#     board[r][c], V[r][c] = 0, 1

#     while R:
#         v, e, [y, x], B = R.pop(0)
#         if not any(sum(B, [])):
#             return v

#         L = []
#         for i in range(4):
#             if B[y][i]:
#                 if [i, y] not in L and i != x:
#                     L.append([i, y])
#             if B[i][x]:
#                 if [x, i] not in L and i != y:
#                     L.append([x, i])

#         for a, b in L + [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
#             if {a, b} < S:
#                 if not B[b][a]:
#                     if not V[b][a]:
#                         V[b][a] = 1
#                         R.append([v+1, e, [b, a], B])
#                 else:
#                     if e == B[b][a]:
#                         R.append([v+2, 0, [b, a], B[:b] +
#                                  [B[b][:a]+[0]+B[b][a+1:]]+B[b+1:]])
#                         V = [[0]*4 for _ in range(4)]
#                     elif not e:
#                         R.append([v+2, B[b][a], [b, a], B[:b] +
#                                  [B[b][:a]+[0]+B[b][a+1:]]+B[b+1:]])
#                         V = [[0]*4 for _ in range(4)]
#                     else:
#                         R.append([v+1, e, [b, a], B])


# print(solution([[1, 0, 0, 3], [2, 4, 0, 4], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [
      0, 0, 0, 2], [3, 0, 1, 0]], 1, 0), 14)
# print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [
#       0, 1, 0, 0], [2, 0, 0, 3]], 0, 1), 16)
# print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [
#       0, 2, 1, 5], [3, 0, 6, 4]], 0, 0), 32)

# l, r, u, d = 1, 1, 1, 1
# while x+r < 4:
#     if board[y][x+r]:
#         r += 1
#         break
#     r += 1
# while x-l >= 0:
#     if board[y][x-l]:
#         l += 1
#         break
#     l += 1
# while y+d < 4:
#     if board[y+d][x]:
#         d += 1
#         break
#     d += 1
# while y-u >= 0:
#     if board[y-u][x]:
#         u += 1
#         break
#     u += 1
# l, r, u, d = l-1, r-1, u-1, d-1
