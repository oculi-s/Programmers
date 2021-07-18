def solution(n, k):
    k -= 1
    t = n-1
    f = 1
    while t:
        f *= t
        t -= 1
    t = n-1
    s = list(range(1,n+1))
    a = [s.pop(k//f)]
    while t:
        k %= f
        f = int(f/t)
        t -= 1
        a.append(s.pop(k//f))
    return a

print(solution(4,20))