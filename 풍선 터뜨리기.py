# def solution(a):
#     s = {0:[a],1:[]}
#     while len([s[0] + s[1]][0][0]) > 1:
#         t = {0:[],1:[]}
#         for x in s[0]:
#             for i in range(len(x)):
#                 v = x[:i] + x[i+1:]
#                 if v not in t[0] and v not in t[1]:
#                     if i:
#                         t[x[i] < x[i-1]].append(v)
#                     if i < len(x)-1:
#                         t[x[i] < x[i+1]].append(v)
#         for x in s[1]:
#             for i in range(len(x)):
#                 v = x[:i] + x[i+1:]
#                 if v not in t[0] and v not in t[1]:
#                     if i:
#                         if x[i] > x[i-1]:
#                             t[0].append(v)
#                     if i < len(x) - 1:
#                         if x[i] > x[i+1]:
#                             t[0].append(v)
#         s = t
#     return len([s[0]+s[1]][0])

def solution(a):
    t = 2
    m, n = a[0],min(a[2:])
    for i in range(1,len(a)-1):
        if a[i-1] > a[i] or a[i+1] > a[i]:
            if n == a[i]:
                n = min(a[i+1:])
            if m > a[i]:
                m = a[i]
                t += 1
            elif n > a[i]:
                t += 1
    return t

# def solution(a):
#     t = 2
#     m = a[0]
#     n = [min(a[2:])]
#     for i in range(len(a)-1):
#         if n[-1] == a[i]:
#             n.append(min(a[i+1:]))
#         else:
#             n.append(n[-1])
#     print(n)
#     for i in range(1,len(a)-1):
#         if a[i-1] > a[i] or a[i+1] > a[i]:
#             if m > a[i]:
#                 m = a[i]
#                 t += 1
#             elif n[i+1] > a[i]:
#                 t += 1
#     return t

def solution(a):
    m, n = a[0], a[-1]
    v = [1] + [0] * (len(a)-2) + [1]
    for i in range(len(a)-2,0,-1):
        if n > a[i]:
            n = a[i]
            v[i] = 1
    for i in range(1,len(a)-1):
        if m > a[i]:
            m = a[i]
            v[i] = 1
    return sum(v)

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))