def solution(strings, n):
    answer = sorted(sorted(strings),key=lambda x:x[n])
    return answer

print(solution(["sun", "bed", "car"],1))