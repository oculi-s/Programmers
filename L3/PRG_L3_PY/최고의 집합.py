def solution(n, s):
    q, r = s//n, s % n
    if not q:
        return [-1]
    else:
        return [q] * (n - r) + [q+1] * r
        

print(solution(2, 9))
print(solution(6, 9))
print(solution(2, 8))
print(solution(2, 1))
