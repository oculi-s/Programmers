# def solution(land):
#     n = len(bin(2**len(land))[2:]) - 1
#     m = 0
#     a = []
#     for i in range(2**(2*len(land))):
#         s = bin(i)[2:].zfill(n*2)
#         go = True
#         t = []
#         for j in range(n):
#             k = int('0b'+s[j:j+2],2)
#             if k == int('0b'+s[j+2:j+4],2):
#                 go = False
#                 break
#             else:
#                 t += [k]
#         if go:
#             a.append(t)
#     for s in a:
#         t = 0
#         for j in range(n):
#             t += land[j][s[j]]
#         if t > m:
#             m = t
#     return m

# def comb(s,t,self,n,r):
#     if r == 0:
#         if s != ''.join(t):
#             self.append(''.join(t))
#     elif n >= r:
#         t[r-1] = s[n-1]
#         comb(s,t,self,n-1,r-1)
#         comb(s,t,self,n-1,r)

# def solution(land):
#     k = {bin(x)[2:].zfill(2):x for x in range(4)}
#     d = ['0000','1111','0101','1010']

#     r = [bin(x)[2:].zfill(len(land)*2) for x in range(2**(2*len(land)))]
#     r = [x for x in r if not any(y in x for y in d)]
#     l = len(r[0])//2

#     a = 0
#     for x in r:
#         v = sum(land[i][k[x[2*i:2*i+2]]] for i in range(l))
#         if v > a:
#             a = v
#     return a

def solution(land):
    r = list(range(4))
    while len(land) > 1:
        r1, r2 = land.pop(), land.pop()
        n = []
        for i in r:
            t = []
            for j in r[:i] + r[i+1:]:
                t.append(r2[i] + r1[j])
            n.append(max(t))
        land.append(n)
    return max(n)


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
# print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))
