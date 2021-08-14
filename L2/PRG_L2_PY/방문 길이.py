def solution(dirs):
    d = [[0,0]]
    for x in dirs:
        p = list(d[-1])
        if x == 'L':
            p[0] -= (p[0] > -5)
        elif x == 'R':
            p[0] += (p[0] < 5)
        elif x == 'U':
            p[1] += (p[1] < 5)
        elif x == 'D':
            p[1] -= (p[1] > -5)
        if p != d[-1]:
            d.append(p)
    t = []
    for x in zip(d[:-1],d[1:]):
        if x not in t and (x[1],x[0]) not in t:
            t.append(x)
    return len(t)

# print(solution("LLLLRLRLRLL"))
# print(solution("UUUUDUDUDUUU"))
# print(solution("LURDLURDLURDLURDRULD"))
print(solution("RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU"))
# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
# print(solution("UDU"))
# print(solution("LRLRL"))