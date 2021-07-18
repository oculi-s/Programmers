# from math import comb as C
# def solution(n):
#     r = 1000000007
#     return int(sum(C(n-x, x) % r for x in range(n//2+1)) % r)

def solution(n):
    if n < 3:
        return n
    else:
        a, b, r = 1, 2, 1000000007
        for _ in range(n-2):
            a, b = b, (a + b) % r
        return b

print(solution(6))