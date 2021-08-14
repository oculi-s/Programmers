def solution(d, budget):
    d += [1000001]
    d.sort(reverse=True)
    for i in range(len(d)):
        budget -= d.pop()
        if budget < 0 or not d:
            return i

print(solution([1],10))