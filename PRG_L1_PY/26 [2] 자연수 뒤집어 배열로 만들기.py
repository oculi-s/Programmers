def solution(n):
    answer = [int(x) for x in reversed(list(str(n)))]
    return answer

print(solution(12345))