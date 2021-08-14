def solution(s):
    answer = not sum([-1 if x in "pP" else x in "yY" for x in s])
    return answer

print(solution(''))