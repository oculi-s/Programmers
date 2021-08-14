def solution(s):
    c = {x: s.count(x) for x in '({[]})'}
    if c['('] != c[')'] or c['['] != c[']'] or c['{'] != c['}']:
        return 0
    d = {x: x in '({[' for x in '({[]})'}

    i, t, tt = 0, 0, 0
    s = list(s)
    while True:
        a, s = s[:i], s[i:]
        while a and s:
            if not d[a[-1]] or d[s[0]]:
                break
            if '({['.index(a.pop()) != ')}]'.index(s.pop(0)):
                return 0
        t += i and not a
        tt += i and not a
        if s:
            if not d[s[0]]:
                t -= tt
                tt = 0
            s = a + s

            i, j = 0, 0
            while not d[s[i]]:
                i += 1
            s = s[i:] + s[:i]
            while d[s[-j-1]]:
                j += 1
            s = s[-j:] + s[:-j]

            i = 0
            while d[s[i]]:
                i += 1
        else:
            return t

print(solution("}]()[{"))
# print(solution("({[]})}{"))
# print(solution('(){[()]}]['))
# print(solution('({[]})}{'))
# print(solution('[(])'))
print(solution('](){}][{}['))
