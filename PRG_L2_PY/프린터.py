def solution(priorities, location):
    p = list(enumerate(priorities))
    d = dict()
    c = 0
    while(p):
        x = p.pop(0)
        if p:
            if x[1] < max([x[1] for x in p]):
                p.append(x)
            else:
                c += 1
                d[x[0]] = c
        else:
            c += 1
            d[x[0]] = c
    return d[location]