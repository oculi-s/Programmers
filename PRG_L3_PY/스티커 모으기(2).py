def solution(sticker):
    c = [[]]
    L = len(sticker)
    for s in range(L):
        t = []
        for x in c:
            if (s or L) -1 not in x and (s+1) % L not in x:
                t.append(x+[s])
        c += t
    t = []
    for x in c:
        t.append(sum(sticker[i] for i in x))
    return max(t)
        



# print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1,3,2,5,4]))