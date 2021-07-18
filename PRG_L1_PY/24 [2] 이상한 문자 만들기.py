def solution(s):
    answer = ' '.join([''.join([x[i].lower() if i%2 else x[i].upper() for i in range(len(x))]) for x in s.split(' ')])
    return answer

print(solution('tryasdf   asdf'))