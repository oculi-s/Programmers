def solution(s):
    answer = (len(s) == 4 or len(s) == 6) and s.isdigit()
    return answer