def solution(n, lost, reserve):
    answer = [0]*(n+2)
    for l in lost:
        answer[l] -= 1
    for r in reserve:
        answer[r] += 1
    for i in range(1,len(answer)-1):
        if answer[i] == -1:
            if answer[i-1] == 1:
                answer[i] = 0
                answer[i-1] = 0
            elif answer[i+1] == 1:
                answer[i] = 0
                answer[i+1] = 0
    answer = sum([x>=0 for x in answer[1:-1]])
    return answer
print(solution(5,[1,2,3],[1,3,5]))