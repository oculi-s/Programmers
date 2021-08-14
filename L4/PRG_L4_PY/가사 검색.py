# def solution(words, queries):
#     W = [[] for _ in range(10001)]
#     for w in words:
#         W[len(w)].append(w)
#     A = []
#     for q in queries:
#         t = q.count('?')
#         if W[len(q)]:
#             if q[0]=='?':
#                 v = [w[t:] for w in W[len(q)]].count(q[t:])
#             else:
#                 v = [w[:-t] for w in W[len(q)]].count(q[:-t])
#         A.append(v)
#     return A

# def solution(words, queries):
#     M = 10001
#     L, R, C = [[]]*M, [[]]*M, [0]*M
#     for w in words:
#         C[len(w)] += 1
#     for w in words:
#         l = len(w)
#         if C[l] == 1:
#             L[l] = {w[:i]:1 for i in range(l)}
#             R[l] = {w[-i:]:1 for i in range(l)}
#             continue
#         if not L[l]:
#             L[l] = dict()
#             R[l] = dict()
#         for i in range(1, l):
#             if w[:i] not in L[l]:
#                 L[l][w[:i]] = 1
#             else:
#                 L[l][w[:i]] += 1
#             if w[-i:] not in R[l]:
#                 R[l][w[-i:]] = 1
#             else:
#                 R[l][w[-i:]] += 1
#     A = []
#     for q in queries:
#         l, t, v = len(q), q.count('?'), 0
#         if l == t:
#             v = C[l]
#         elif q[0] == '?':
#             if q[t:] in R[l]:
#                 v = R[l][q[t:]]
#         elif q[-1] == '?':
#             if q[:-t] in L[l]:
#                 v = L[l][q[:-t]]
#         A.append(v)
#     return A
    
# def solution(words, queries):
#     M = 10001
#     C = [[] for _ in range(M)]
#     for w in words:
#         l = len(w)
#         C[l].append(w)
#     A = [0] * len(queries)
#     T = dict()
#     for i, q in enumerate(queries):
#         l, t = len(q), q.count('?')
#         if q not in T:
#             if l == t:
#                 A[i] = len(C[l])
#             elif C[l]:
#                 if q[0] == '?':
#                     A[i] = [w[t:] for w in C[l]].count(q[t:])
#                 elif q[-1] == '?':
#                     A[i] = [w[:-t] for w in C[l]].count(q[:-t])
#             T[q] = A[i]
#         else:
#             A[i] = T[q]
#     return A

# def solution(words, queries):
#     M = 10001
#     L, R, C = [[]]*M, [[]]*M, [[] for _ in range(M)]
#     for w in words:
#         l = len(w)
#         C[l].append(w)
#         if not L[l]:
#             L[l] = dict()
#             R[l] = dict()
#     for l in range(M):
#         for w in C[l]:
#             for i in range(1, l):
#                 if w[:i] not in L[l]:
#                     L[l][w[:i]] = 1
#                 else:
#                     L[l][w[:i]] += 1
#                 if w[-i:] not in R[l]:
#                     R[l][w[-i:]] = 1
#                 else:
#                     R[l][w[-i:]] += 1
#     A = []
#     for q in queries:
#         l, t, v = len(q), q.count('?'), 0
#         if l == t:
#             v = len(C[l])
#         elif C[l]:
#             if q[0] == '?':
#                 if q[t:] in R[l]:
#                     v = R[l][q[t:]]
#             elif q[-1] == '?':
#                 if q[:-t] in L[l]:
#                     v = L[l][q[:-t]]
#         A.append(v)
#     return A

class node:
    def __init__(self):
        self.v = 0
        self.child = dict()

class tree:
    def __init__(self):
        self.head = node()
    def push(self,w,d):
        t = self.head
        if not d:
            w = reversed(w)
        for x in w:
            if x not in t.child:
                t.child[x] = node()
            t = t.child[x]
            t.v += 1
    def find(self,q,d):
        n = self.head
        if not d:
            q = reversed(q)
        for x in q:
            if x == '?':
                return n.v
            if x not in n.child:
                return 0
            n = n.child[x]

def solution(words, queries):
    M = max(map(len,words))+10
    L = [tree() for _ in range(M)]
    R = [tree() for _ in range(M)]
    C = [0 for _ in range(M)]
    for w in words:
        L[len(w)].push(w,1)
        R[len(w)].push(w,0)
        C[len(w)] += 1
    A = []
    for q in queries:
        if q[0] == '?' and q[-1] == '?':
            A.append(C[len(q)])
        elif q[0] == '?':
            A.append(R[len(q)].find(q,0))
        else:
            A.append(L[len(q)].find(q,1))
    return A

print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
# print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "?????", "fr???", "fro???", "pro?"]))

