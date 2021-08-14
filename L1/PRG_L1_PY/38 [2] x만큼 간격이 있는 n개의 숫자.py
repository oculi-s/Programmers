def solution(x, n):
    if not x:
        return [x]*n
    answer = list(range(x,x*n+(x>0 or -1),x))
    return answer

print(solution(0,3))