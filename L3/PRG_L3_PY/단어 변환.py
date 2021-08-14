def solution(begin, target, words):
    if not target in words:
        return 0

    g = dict()
    s,m,e = [],[],[]
    for i in range(len(words)):
        w = words[i]
        if w == target:
            continue
        if sum(x != y for x,y in zip(begin,w)) == 1:
            s.append(w)
        elif sum(x != y for x,y in zip(target,w)) == 1:
            e.append(w)
        else:
            m.append(w)
    words = [begin] + s + m + e + [target]
    w = dict(enumerate(words))

    for b in w:
        l = set()
        for k in w.keys():
            if sum(x != y for x,y in zip(w[b],w[k])) == 1 and k > b:
                l.add(k)
        g[b] = l
    if words.index(target) + 1 in g[0]:
        return 1

    s = [0]
    v = []
    m = []
    while s:
        n = s.pop()
        if n not in v:
            v.append(n)
            s += g[n] - set(v)
            if not g[n]:
                if n + 1 == len(g):
                    m.append(len(v) - 1)
                while v and len(g[n]) < 2:
                    n = v.pop()
                v.append(n)
    return min(m)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)