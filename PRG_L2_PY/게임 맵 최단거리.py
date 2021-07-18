# m = {'l':(-1,0),'r':(1,0),'d':(0,1),'u':(0,-1)}
# h = {'':'','l':'r','r':'l','u':'d','d':'u'}
# a = ''
# p = (1,1)
# t = []
# l = [17]

# def solution(maps):
#     if not maps[3][4] + maps[4][3]:
#         return -1
#     maps = [[0]*7] + [[0]+x+[0] for x in maps] + [[0]*7]
#     # 0,-1 down -1,0 left 1,0 right (0,1) up
#     # move position direction
#     c = 0
#     l = f(maps,p,a,c)
#     print(min(l))

# def f(maps,p,a,c):
#     while p != (5,5) and c < 18:
#         d = [d for d in m if maps[p[1]+m[d][1]][p[0]+m[d][0]] and d != h[a]]
#         if not d:
#             break
#         if d:
#             a = d.pop()
#             p = p[0]+m[a][0],p[1]+m[a][1]
#             c += 1
#             for x in d:
#                 if c < min(l):
#                     t.append((p,x,c))
#     if c < min(l):
#         l.append(c+1)
#     if t:
#         p,a,c = t.pop()
#         print(l,p,a,c,t)
#         f(maps,p,a,c)
#     return l

# def solution(maps):
#     if not maps[3][4] + maps[4][3]:
#         return -1
#     maps = [[0]*7] + [[0]+x+[0] for x in maps] + [[0]*7]
#     m = {'l':(-1,0),'r':(1,0),'d':(0,1),'u':(0,-1)}
#     h = {'':'','l':'r','r':'l','u':'d','d':'u'}
#     a = ''
#     p = (1,1)
#     c = 0
#     while p != (5,5):
#         d = [d for d in m if maps[p[1]+m[d][1]][p[0]+m[d][0]] and d != h[a]]
#         a = d.pop()
#         while maps[p[1]+m[a][1]][p[0]+m[a][0]]:
#             p = p[0]+m[a][0],p[1]+m[a][1]
#             c += 1
#         a =

# def solution(maps):
#     n, m = len(maps), len(maps[0])
#     r = [[(1, 1)]]
#     b = [[0]*(m+2)] + [[0]+x+[0]for x in maps] + [[0]*(m+2)]
#     for p in r:
#         if (n, m) in p:
#             return len(p)
#         else:
#             y, x = p[-1]
#             for y, x in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
#                 if b[y][x]:
#                     if (y, x) not in p:
#                         r.append(p+[(y, x)])
#     return -1

def solution(maps):
    n, m = len(maps), len(maps[0])
    r = [[(n-1, m-1)]]
    v = [[1] * m for _ in range(n)]
    while r:
        p = r.pop(0)
        y, x = p[-1]
        for b, a in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if (b + 1) * (a + 1) and b < n and a < m:
                if maps[b][a]:
                    if (b, a) == (0, 0):
                        return v[y][x] + 1
                    if v[b][a] == 1:
                        r.append(p+[(b, a)])
                        v[b][a] = v[y][x] + 1
    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 1, 1, 1, 1]]	))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	))
