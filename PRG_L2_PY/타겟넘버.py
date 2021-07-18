def solution(numbers, target):
    g = [[-x,x] for x in numbers]
    l = len(numbers)
    a = []
    for i in range(2**l):
        a.append(sum(x[int(y)] for x,y in zip(g,bin(i)[2:].zfill(l))))
    return a.count(target)

print(solution([1,1,1,1,1],3))