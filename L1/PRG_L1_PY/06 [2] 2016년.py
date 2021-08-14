def solution(a, b):
    d = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        b += d[i]
    print(b)
    answer = ["FRI","SAT","SUN","MON","TUE","WED","THU"][(b-1)%7]
    return answer

print(solution(5,24))