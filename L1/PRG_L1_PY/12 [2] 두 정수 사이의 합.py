def solution(a, b):
    answer = sum([x for x in range(min(a,b),max(a,b)+1)])
    return answer