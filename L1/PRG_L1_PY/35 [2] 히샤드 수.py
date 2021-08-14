def solution(x):
    answer = not bool(x % sum([int(a) for a in list(str(x))]))
    return answer

print(solution(12))