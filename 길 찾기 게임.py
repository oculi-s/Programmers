# preorder까지는 성공했지만 시간초과

def solution(nodeinfo):
    X,Y = [max(r) for r in zip(*nodeinfo)]
    B = [[0]*(X+1) for _ in range(Y+1)]
    for x,y in nodeinfo:
        B[y][x] = 1
    C = {i+1:[None,None] for i in range(len(nodeinfo))}
    for y in reversed(range(Y+1)):
        if sum(B[y]):
            for x in range(X+1):
                if B[y][x]:
                    i = nodeinfo.index([x,y]) + 1
                    d = 1
                    while not sum(B[y-d]):
                        d += 1
                    if sum(B[y-d][:x]):
                        l = B[y-d][:x].index(1)
                        if not sum(sum(t[l+1:x]) for t in B[y-d+1:]):
                            C[i][0] = nodeinfo.index([l,y-d]) + 1
                    if sum(B[y-d][x+1:]):
                        r = B[y-d][x+1:].index(1) + x+1
                        if not sum(sum(t[x+1:r]) for t in B[y-d+1:]):
                            C[i][1] = nodeinfo.index([r,y-d]) + 1
    O = nodeinfo.index([B[Y].index(1),Y]) + 1
    s, P = [O], []
    while s:
        n = s.pop(0)
        if n:
            if n not in P:
                P.append(n)
            s = C[n] + s

    x = 0
    I = list(zip(*B))
    while not sum(I[x]):
        x += 1
    O = nodeinfo.index([x,I[x].index(1)]) + 1
    O = C[O][0] or C[O][1] or O
    s, Q = [O], []
    while s:
        n = s.pop(0)
        if n:
            if n not in Q:
                Q.append(n)
            s = s + C[n]
    print(P)
    print(Q)    


    # for t in reversed(B):
    #     print(t)
                

        


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
      [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]	))
