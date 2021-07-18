def solution(n, works):
    works.sort()
    tw = works
    while True:
        v, l = sum(tw) - n, len(tw)
        q, r = v // l, v % l
        i = 0
        while tw[i] <= q:
            i += 1
        tw = tw[i:]
        if not i:
            break
    if v < 0:
        return 0
    w = works[:-len(tw)] + [q] * (l-r) + [q+1] * r
    return sum(x**2 for x in w)

print(solution(3, [1, 1, 6]))
# print(solution(4, [1, 1, 6]))
# print(solution(4, [4, 3, 3]))
# print(solution(4, [1, 6, 3]))
# print(solution(1, [2, 1, 2]))
# print(solution(3, [1, 1]))
