def solution(str1, str2):
    s = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s1 = str1.upper()
    s2 = str2.upper()
    s1 = [x for x in zip(s1[:-1], s1[1:]) if set(x).issubset(s)] or [0]
    s2 = [x for x in zip(s2[:-1], s2[1:]) if set(x).issubset(s)] or [0]

    a = 0
    b = 0
    if len(s1) < len(s2):
        t = s2
        s2 = s1
        s1 = t
    s = list(s1)
    for x in s2:
        if not x in s:
            s.append(x)
    for x in set(s):
        t = (s1.count(x), s2.count(x))
        a += min(t)
        b += max(t)
    return int(a/b*65536)

print(solution('FRANCE','french'))
print(solution('abababaa','ababab'))
print(solution("aa1+aa2", "AAAA12"))
print(solution("aaaa", "aaaaa"))
print(solution('handshake','shake hands'))
print(solution('E=M*C^2','e=m*c^2'))
