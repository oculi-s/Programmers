def solution(n,a,b):
    v = 1
    a -= 1
    b -= 1
    t = 2
    while t < n:
        if a//t == b//t:
            break
        v += 1
        t *= 2
    return v

print(solution(8,4,7))