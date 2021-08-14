def solution(land, P, Q):
    land = sorted(sum(land, []))
    l = len(land)
    e = Q * l // (P + Q)
    return P * (e*land[e] - sum(land[:e])) - Q * ((l-e)*land[e] - sum(land[e:]))


# print(solution([[0, 2], [2, 3]],3,2))
print(solution([[1, 3], [3, 3]],3,2))
print(solution([[1, 2], [2, 3]], 3, 2))
print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))


# from bisect import bisect_left
# def solution(land, P, Q):
#     land = sorted(sum(land,[]))
#     l = len(land)
#     v = (sum(land) - min(land) * l) * Q
#     for i in range(1,Q * l // (P + Q)):
#         j = bisect_left(land,land[0]+i)
#         v += P * j - Q * (l - j)
#     return v
