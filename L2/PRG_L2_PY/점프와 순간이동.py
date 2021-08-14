def solution(n):
    a = 0
    while n:
        if n % 2:
            n -= 1
            a += 1
        n //= 2
    return a
