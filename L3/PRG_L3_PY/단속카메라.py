def solution(routes):
    v = 0
    r = routes
    while r:
        i = min(x[1] for x in r)
        t = []
        for x in r:
            if not (x[0] <= i and i <= x[1]):
                t.append(x)
        r = t
        v += 1
    return v

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))