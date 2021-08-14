def solution(words):
    v = 0
    for w in words:
        i = 1
        while any(w[:i] == x[:i] for x in words if x != w):
            i += 1
        v += len(w[:i])
    return v

def solution(words):
    v = 0
    for i in range(len(words)):
        j = 0
        w = words[i]
        t = words[:i] + words[i+1:]
        while t and j < len(w):
            j += 1
            s = []
            for x in t:
                if w[:j] == x[:j]:
                    s.append(x)
            t = s
        v += j
    return v

def solution(words):
    words.sort()
    w = sorted(words) + ['1']
    v = 0
    hh = 0
    for i in range(len(w)-1):
        h = 1
        while w[i][:h] == w[i+1][:h]:
            h += 1
        v += min(max(h,hh),len(w[i]))
        hh = h
    return v

print(solution(["word","war","warrior","world"]))