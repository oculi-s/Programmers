from itertools import combinations
def solution(distance, rocks, n):
    rocks = [0] + sorted(rocks) + [distance]
    l, r = 1, distance
    while l <= r:
        t = list(rocks)
        m = (l + r) // 2
        t.pop(m)
        if v > d:
            l = m + 1
        else:
            r = m - 1
    return v

# def solution(distance, rocks, n):
#     rocks.sort()
#     rocks = [0] + rocks + [distance]
#     d = [x-y for x,y in zip(rocks[1:],rocks)]
#     r = [d]
#     n = len(d) - n
#     a = set()
#     while len(r[0]) > n:
#         t = []
#         for x in r:
#             for i in range(len(x)-1):
#                 v = x[:i] + [x[i] + x[i+1]] + x[i+2:]
#                 if not v in r:
#                     t.append(v)
#         r = t
#         print(r)
#     for x in r:
#         a.add(min(x))
#     return max(a)

# 최솟값의 최댓값
# 2 9 3 3 4 4
# 전체의 최대가 한 집합의 최소가 될 수 있는가?
# 9가 한 집합의 최소가 될 수 있는가
# 모든 9와 최소가 붙어있다면 9는 한 집합의 최소가 될 수 없음
# def solution(distance, rocks, n):
#     rocks = [0] + sorted(rocks) + [distance]
#     d = [x-y for x,y in zip(rocks[1:],rocks)]
#     d = [2,9,3,3,3,9]
#     r = sorted(set(d))
#     t = 0
#     while r:
#         x = r.pop()
#         for i in range(1,len(d)):
#             if d[i] == x and r[0] not in d[i-1:i+2]:
#                 t = x
#                 break
#         if t:
#             a = list(d)
#             for i in range(len(a)):
#                 if a[i] == t:
#                     a[i] = max(a)
#             if sum(sorted(a)[:n+1]) > t:
#                 return t
#             else:
#                 print(a,r,t)
#             print(a, r, t)
#             break
    # return max(d)


print(solution(25, [2, 14, 11, 21, 17], 2))
