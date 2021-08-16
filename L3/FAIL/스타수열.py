def solution(a):
    if len(a) == 1:
        return 0
    s = {''.join(str(x) for x in a)}
    while s:
        x = s.pop()
        if not len(x) % 2:
            t = [{a,b} for a,b in zip(x[::2],x[1::2]) if a != b]
            if len(t)*2 == len(x) and set.intersection(*t):
                return len(x)
        for i in range(len(x)):
            s.add(x[:i]+x[i+1:])

print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))