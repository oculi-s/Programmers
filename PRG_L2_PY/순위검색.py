# def solution(info, query):
#     q = {}
#     for x in info:
#         x = x.split(' ')
#         y = tuple(x[:-1])
#         if y in q:
#             q[y] += [int(x[-1])]
#         else:
#             q[y] = [int(x[-1])]
#     a = {}
#     for x in query:
#         x = x.replace(' and','').split(' ')
#         y = tuple(x)
#         a[y] = 0
#         for z in q:
#             if set(x[:-1]) - set(z) in [{'-'}, set()]:
#                 a[y] += sum(w >= int(x[-1]) for w in q[z])
#     return list(a.values())

# def solution(info, query):
#     i = [x.split(' ') for x in info]
#     q = [set(y.replace('- ','').replace('and ','').strip().split(' ')) for y in query]
#     a = []
#     for y in q:
#         v = 0
#         for x in i:
#             t = y - set(x[:-1])
#             if ''.join(t).isdigit():
#                 if int(t.pop()) <= int(x[-1]):
#                     v += 1
#         a.append(v)
#     return a

# def solution(info, query):
#     i = [x.split(' ') for x in info]
#     q = [y.replace(' ','').replace('-','').replace('and','').strip() for y in query]

#     a = []
#     for y in q:
#         v = 0
#         for x in i:
#             t = y
#             for z in x[:-1]:
#                 t = t.replace(z,'')
#             if t.isdigit():
#                 if int(t) <= int(x[-1]):
#                     v += 1
#         a.append(v)
#     return a

# def solution(info, query):
#     i = [x.split(' ') for x in info]
#     q = [y.replace(' ','').replace('-','').replace('and','').strip() for y in query]
#     print(i,q)

#     a = []
#     for y in q:
#         v = 0
#         for x in i:
#             t = y
#             for z in x[:-1]:
#                 t = t.replace(z,'')
#             if t.isdigit():
#                 if int(t) <= int(x[-1]):
#                     v += 1
#         a.append(v)
#     return a

# def solution(info, query):
#     i = {'i'+str(k):{'a'+str(j):y for j,y in enumerate(x.split(' '))} for k,x in enumerate(info)}
#     q = {'q'+str(k):{'a'+str(j):y.strip() for j,y in enumerate(x.split('and'))} for k,x in enumerate(query)}
#     for x in q.values():
#         x['a3'], x['a4'] = x['a3'].split(' ')

#     a = {x:dict() for x in q.keys()}
#     for m,y in q.items():
#         for n,x in y.items():
#             if x == '-':
#                 continue
#             else:
#                 if n == 'a4':
#                     for l,z in i.items():
#                         if int(z[n]) < int(x):
#                             a[m][l] = False
#                 else:
#                     for l,z in i.items():
#                         if x not in z[n]:
#                             a[m][l] = False
#     return [len(i) - len(x) for x in a.values()]

# def solution(info, query):
#     d = [int(i.split()[-1]) for i in info]
#     i = {j: [set(x.split(' ')[:-1]), d] for j, (d, x) in enumerate(zip(d, info))}
#     d = [int(q.split()[-1]) for q in query]
#     q = {j: [set([y.strip().split(' ')[0] for y in x.split('and') if '-' not in y]), d] for j, (d, x) in enumerate(zip(d, query))}

#     a = {x: dict() for x in q.keys()}
#     for m, y in q.items():
#         for n, x in i.items():
#             a[m][n] = not (y[0] - x[0]) and y[1] <= x[1]
#     return [sum(x.values()) for x in a.values()]

# def solution(info, query):
#     d = [int(i.split()[-1]) for i in info]
#     i = {j: [set(x.split(' ')[:-1]), d] for j, (d, x) in enumerate(zip(d, info))}
#     d = [int(q.split()[-1]) for q in query]
#     q = {j: [set([y.strip().split(' ')[0] for y in x.split('and') if '-' not in y]), d] for j, (d, x) in enumerate(zip(d, query))}

#     return [sum(not (y[0] - x[0]) and y[1] <= x[1] for x in i.values()) for y in q.values()]

# def solution(info, query):
#     d = [int(i.split()[-1]) for i in info]
#     i = [[set(x.split()[:-1]), d] for d, x in zip(d, info)]
#     d = [int(q.split()[-1]) for q in query]
#     q = [[set(x.split()[:-1]) - {'-','and'}, d] for d, x in zip(d, query)]

#     return [sum(not (y[0] - x[0]) and y[1] <= x[1] for x in i) for y in q]

# def solution(info, query):
#     i = [set(x.split()[:-1]) for x in info]
#     q = [set(x.split()[:-1]) - {'-', 'and'} for x in query]
#     a = [int(x.split()[-1]) for x in info]
#     b = [int(x.split()[-1]) for x in query]

#     return [sum(not (y - x) and n <= m for x, m in zip(i, a)) for y, n in zip(q, b)]

# def solution(info, query):
#     i = sorted([x.split() for x in info], key=lambda c: int(c[-1]))
#     q = [x.split() for x in query]

#     a = [int(x.pop()) for x in i]
#     b = [int(x.pop()) for x in q]
#     j = [sorted(a + [m]).index(m) for m in b]
#     i = [set(x) for x in i]
#     q = [set(x) - {'-', 'and'} for x in q]
    
#     c = [sum(not(x-y) for y in i[j.pop(0):]) for x in q]
#     return c

# def solution(info, query):
#     a = [['-','cpp','java','python'],['-','backend','frontend'],['-','junior','senior'],['-','chicken','pizza']]
#     c = dict()
#     for x in a:
#         c.update({v:bin(k)[2:].zfill(2) for k,v in enumerate(x)})

#     i = sorted([x.split() for x in info], key=lambda c: int(c[-1]))
#     a = [int(x.pop()) for x in i]
#     b = [int(x.split()[-1]) for x in query]
    
#     j = [sorted(a + [m]).index(m) for m in b]
#     i = [''.join(x) for x in i]
#     q = [''.join(x.replace('and','').split()[:-1]) for x in query]

#     i = ''.join(i)
#     q = ''.join(q)
#     for x in c:
#         i = i.replace(x,c[x])
#         q = q.replace(x,c[x])

#     q = [q[j:j+8] for j in range(0,len(q),8)]
#     l = len(i)//8
#     d = [[k, int(x*(l-k),2),int(i[k*8:],2)] for x,k in zip(q,j)]

#     c = []
#     while d:
#         k, x, y = d.pop(0)
#         m = bin(x | y)[2:].zfill(8*(l-k))
#         n = bin(y)[2:].zfill(8*(l-k))
#         print(m,n)
#         while m:
#             if m[:8] != n[:8]:
#                 k -= 1
#             m = m[8:]
#             n = n[8:]
#     return [l-k for k in j]

# def solution(info, query):
#     i = sorted([x.split() for x in info], key=lambda c: int(c[-1]))
#     q = [x.replace('and','').replace('-','').split() for x in query]
#     a = [int(x.pop()) for x in i]
#     b = [int(x.pop()) for x in q]

#     j = [sorted(a + [m]).index(m) for m in b]
#     i = [set(x) for x in i]
#     q = [set(x) for x in q]
#     d = [sum(not x-y for y in i[k:]) for x,k in zip(q,j)]
#     return d

# import bisect
# def solution(info, query):
#     i = sorted([x.split() for x in info], key=lambda c: int(c[-1]))
#     q = [x.replace('and','').replace('-','z').split() for x in query]

#     a = [int(x.pop()) for x in i]
#     b = [int(x.pop()) for x in q]
    
#     j = [bisect.bisect(a,m-1) for m in b]
    
#     d = [sorted(i[k:]) for k in j]
#     c = []
#     for x in d:
#         y = q.pop(0)
#         print(x,y)
#         x = bisect.bisect_left(x,y)
#         c.append(x)
#     return c

from bisect import bisect, insort
def solution(info, query):
    d = dict()
    for x in info:
        x = x.split()
        x, y = ' '.join(x[:4]), int(x[4])
        if x not in d:
            d[x] = [y]
        else:
            insort(d[x],y)
    c = []
    for x in query:
        x = x.replace(' and','').split()
        x, y = x[:4], int(x[4]) - 1
        t = 0
        for z in d:
            if set(x) - {'-'} <= set(z.split()):
                t += len(d[z]) - bisect(d[z],y)
        c.append(t)
    return c

# def solution(info, query):
#     i = sorted([x.split() for x in info], key=lambda c: int(c[-1]))
#     q = [x.replace('and','').replace('-','').split() for x in query]

#     a = [int(x.pop()) for x in i]
#     b = [int(x.pop()) for x in q]
#     j = [bisect.bisect(a,m-1) for m in b]
#     d = [i[k:] for k in j]

#     c = []
#     for x in d:
#         y = q.pop(0)
#         for z in y:
#             nx = []
#             for w in x:
#                 while w:
#                     if w[0] == z:
#                         nx.append(w[1:])
#                         break
#                     else:
#                         w = w[1:]
#             x = nx
#         c.append(len(x))
#     return c

print(solution(
    ["java backend junior pizza 150",
     "python frontend senior chicken 210",
     "python frontend senior chicken 150",
     "cpp backend senior pizza 260",
     "java backend junior chicken 80",
     "python backend senior chicken 50"],

    ["java and backend and junior and pizza 100",
     "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250",
     "- and backend and senior and - 150",
     "- and - and - and chicken 100",
     "- and - and - and - 150"]))
