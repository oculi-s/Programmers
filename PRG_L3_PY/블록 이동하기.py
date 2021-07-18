# def D(P, O, B):
#     x, y = zip(*set([*O, *P]))
#     x, y = {x.count(t): t for t in set(x)}, {y.count(t): t for t in set(y)}
#     return not B[y[1]][x[1]]


# def solution(board):
#     N = len(board)
#     R = [[((0, 0), (1, 0))]]
#     S = set(range(N))

#     while R:
#         r = R.pop(0)
#         if (N-1, N-1) in r[-1]:
#             return len(r)-1

#         (ax, ay), (bx, by) = r[-1]
#         for (mx, my), (nx, ny) in [((ax+1, ay), (bx+1, by)), ((ax-1, ay), (bx-1, by)), ((ax, ay+1), (bx, by+1)), ((ax, ay-1), (bx, by-1))]:
#             if {mx, my, nx, ny} < S:
#                 if not (board[my][mx]+board[ny][nx]):
#                     if ((mx, my), (nx, ny)) not in r and ((nx, ny), (mx, my)) not in r:
#                         R.append(r + [((mx, my), (nx, ny))])
#         t = bx == ax
#         for (mx, my), (nx, ny) in [((bx+t, by+(1-t)), (bx, by)), ((bx-t, by-(1-t)), (bx, by)), ((ax, ay), (ax+t, ay+(1-t))), ((ax, ay), (ax-t, ay-(1-t)))]:
#             if {mx, my, nx, ny} < S:
#                 if not (board[my][mx]+board[ny][nx]):
#                     if D(((mx, my), (nx, ny)), ((ax, ay), (bx, by)), board):
#                         if ((mx, my), (nx, ny)) not in r and ((nx, ny), (mx, my)) not in r:
#                             R.append(r + [((mx, my), (nx, ny))])

# d,s = 1,1 가로 --> 세로
# x,y,0 x+1,y+1
# x,y-1,0 x+1,y-1
# x+1,y,0 x,y+1
# x+1,y-1,0 x,y-1

# d,s = 0, -1 세로 --> 가로
# x,y,1 x+1,y+1
# x,y+1,1 x+1,y
# x-1,y,1 x-1,y+1
# x-1,y+1,1 x-1,y


# def solution(board):
#     N = len(board)
#     R = [[[0, 0, 1]]]
#     S = set(range(N))

#     while R:
#         r = R.pop(0)
#         if r[-1][:2] in [[N-1, N-2], [N-2, N-1]]:
#             print(r)
#             return len(r)-1

#         x, y, d = r[-1]
#         s = d or -1
#         for a, b in [[x, y], [x, y-s], [x+s, y], [x+s, y-s]]:
#             if [a, b, 1-d] not in r:
#                 if {a, b, a+(1-d), b+d} < S:
#                     if not (board[b][a] + board[b+d][a+(1-d)]):
#                         q = d*b+(1-d)*y+(y == b)
#                         p = d*x+(1-d)*a+(x == a)
#                         if not board[q][p]:
#                             if {p, q} < S:
#                                 R.append(r+[[a, b, 1-d]])

#         for a, b in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
#             if [a, b, d] not in r:
#                 if {a, b, a+d, b+(1-d)} < S:
#                     if not (board[b][a] + board[b+(1-d)][a+d]):
#                         R.append(r + [[a, b, d]])

def solution(board):
    N = len(board)
    R = [[0,[0, 0, 1]]]
    S = set(range(N))
    V = [[[0]*N for _ in range(N)] for _ in range(2)]

    while R:
        v,[x,y,d] = R.pop(0)
        if [x,y,d] in [[N-1, N-2, 0], [N-2, N-1, 1]]:
            return v

        s = d or -1
        for a, b in [[x, y], [x, y-s], [x+s, y], [x+s, y-s]]:
            if {a, b, a+(1-d), b+d} < S:
                if not V[d][b][a]:
                    if not (board[b][a] + board[b+d][a+(1-d)]):
                        q = d*b+(1-d)*y+(y == b)
                        p = d*x+(1-d)*a+(x == a)
                        if not board[q][p]:
                            if {p, q} < S:
                                V[d][b][a] = 1
                                R.append([v+1,[a, b, 1-d]])

        for a, b in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            if {a, b, a+d, b+(1-d)} < S:
                if not V[1-d][b][a]:
                    if not (board[b][a] + board[b+(1-d)][a+d]):
                        V[1-d][b][a] = 1
                        R.append([v+1,[a, b, d]])


# print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
#       0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]	))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
