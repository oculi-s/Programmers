# def solution(gems):
#     s = set(gems)
#     a = len(set(gems))
#     while True:
#         for i in range(len(gems)-a+1):
#             if s == set(gems[i:i+a]):
#                 return [i+1,i+a]
#         a += 1

# def solution(gems):
#     while gems[-1] in gems[:-1]:
#         gems.pop()
#     s = 0
#     while gems[s] in gems[s+1:]:
#         s += 1
#     return [s+1,len(gems)]

# from collections import deque
# def solution(gems):
#     s = set(gems)
#     a = len(set(gems))
#     while True:
#         print(len(gems)-a+1)
#         for i in range(len(gems)-a+1):
#             print(gems[i:i+a])
#             if set(gems[i:i+a]) == s:
#                 return [i+1,i+a]
#         a += 1

# from bisect import bisect
# def solution(gems):
#     a = {x: [] for x in set(gems)}
#     for i, x in enumerate(gems):
#         a[x].append(i+1)

#     m, n = len(gems)+1, 0
#     for x in list(a.keys()):
#         m = min(a[x][-1], m)
#         n = max(a[x][0], n)
#     for x in list(a.keys()):
#         if m in a[x] or n in a[x]:
#             a.pop(x)
#         else:
#             for b in a[x]:
#                 if m <= b and b <= n:
#                     a.pop(x)
#                     break
#     for x in list(a.keys()):
#         i, j = bisect(a[x], m), bisect(a[x], n)
#         b = m-a[x][i-1]
#         c = a[x][j]-n
#         if c <= b:
#             n = a[x][j]
#         else:
#             m = a[x][i-1]
#     return [min(m, n), n]


from bisect import bisect
def solution(gems):
    a = {x:[] for x in set(gems)}
    for i, x in enumerate(gems):
        a[x].append(i+1)
    m, n = len(gems),1

    for x in set(gems):
        if len(a[x]) == 1:
            m = min(a[x][0],m)
            n = max(a[x][0],n)
            a.pop(x)
    for x in list(a.keys()):
        if a[x][-1] < m:
            m = a[x][-1]
        elif a[x][0] > n:
            n = a[x][0]
    for x in list(a.keys()):
        if m in a[x] or n in a[x]:
            a.pop(x)
        else:
            for b in a[x]:
                if m < b and b < n:
                    a.pop(x)
                    break
    if m > n:
        return [n, n]
    for x in list(a.keys()):
        i, j = bisect(a[x],m), bisect(a[x],n)
        b = m-a[x][i-1]
        c = a[x][j]-n

        if c < b:
            n = a[x][j]
        else:
            m = a[x][i-1]
    return [m,n]

print(bisect([1, 2, 3, 4, 5], 4))


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]), [3, 7])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]), [1, 5])
print(solution(["AC", 'AC', "AA", "AB", "AD", "AA", 'AE', "AC", "AC"]), [4, 8])
print(solution(['a', 'a', 'a']), [1, 1])
print(solution(["A", "A", "B"]), [2, 3])
