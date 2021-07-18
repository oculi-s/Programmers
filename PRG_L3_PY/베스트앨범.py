def solution(genres, plays):
    d = {x:[] for x in set(genres)}
    for i,x in enumerate(plays):
        d[genres[i]].append([i,x])
    s = dict()
    for x in d:
        s[x] = sum(list(zip(*d[x]))[1])
        d[x] = sorted(d[x],key=lambda c:c[1],reverse=True)
    s = sorted(s.items(),key=lambda c:c[1])
    s = list(list(zip(*s))[0])
    a = []
    while s:
        a += list(list(zip(*d[s.pop()]))[0])[:2]
    return a

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))