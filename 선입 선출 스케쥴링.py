def solution(n, cores):
    a = []
    for c in cores:
        a += list(range(0,n+1,c))
    b = {x:a.count(x) for x in range(n)}

    v = 0
    for x in b:
        v += b[x]
        if v >= n:
            return x

print(solution(6,[1,2,3]))