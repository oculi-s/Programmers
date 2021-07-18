# from math import ceil
# def solution(n, stations, w):
#     r = [0] * n
#     for x in stations:
#         for y in range(x-w-1, x+w):
#             if y < n:
#                 r[y] = 1
#     i = 0
#     a = 0
#     while i < n:
#         if r[i]:
#             i += 1
#             continue
#         t = i
#         while not r[t]:
#             t += 1
#             if t == n:
#                 break
#         t -= i
#         a += ceil(t/(2*w+1))
#         i += t
#     return a

from math import ceil
def solution(n, stations, w):
    s, v = 1, 0
    if stations[-1] < n-w:
        stations.append(n+w+1)
    for x in stations:
        d = x-w-s
        s = x+w+1
        v += ceil(d/(2*w+1))
    return v


# print(solution(1,[1],1))
print(solution(11, [4], 1))
# print(solution(16,[9],2))
