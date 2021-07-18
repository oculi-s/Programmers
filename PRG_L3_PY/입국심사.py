# from bisect import bisect
# def solution(n, times):
#     times.sort()
#     t = times[0] * n
#     a = set()
#     for x in times[1:]:
#         tx = x
#         while tx < t:
#             t -= times[0]
#             tx += x
#         a.add(tx)
#     a.add(t)
#     return min(a)

def solution(n, times):
    l, r = min(times), min(times) * n
    while l <= r:
        m = (l + r)//2
        v = sum(m//x for x in times)
        if v < n:
            l = m + 1
        else:
            r = m - 1
    return l

# print(solution(6,[7,10]))
# print(solution(3,[1, 1, 1]))
print(solution(3,[1, 2, 3]))
# print(solution(1,[2, 2]))
# print(solution(7,[2, 3]))
# print(solution(1000000000,[1, 1000000000, 1000000000]))