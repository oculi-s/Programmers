def solution(N, stages):
    answer = {}
    for x in range(1,N+1):
        answer[x] = (stages.count(x))/(len(list(filter(lambda y:y>=x,stages))) or 1)
    return [x[0] for x in sorted(answer.items(),key=lambda x:x[1],reverse=True)]

print(solution(5, [2,1,2,3,2,4,3,3]))