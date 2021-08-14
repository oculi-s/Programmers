def solution(n, m):
    if n > m:
        t = n
        n = m
        m = t
    t = m % n
    mn = m * n
    while t:
        m = n
        n = t
        t = m % n
    answer = [n, int(mn/n)]
    return answer


print(solution(5, 2))
