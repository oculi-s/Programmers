def solution(stones, k):
    l, r = min(stones), max(stones)
    stones = [max(stones)] + stones + [max(stones)]
    while l <= r:
        m = (l + r)//2
        v = 0
        h = 0
        for i,x in enumerate(stones):
            if x >= m:
                if i - h > v:
                    v = i - h
                    if v > k:
                        r = m - 1
                        break
                h = i
        if v <= k:
            l = m + 1
    return l - 1

print(solution(	[2, 4, 5, 3, 2, 1, 4, 2, 9, 1], 3))
