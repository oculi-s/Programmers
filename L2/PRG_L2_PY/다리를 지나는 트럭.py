def solution(bridge_length, weight, truck_weights):
    t = list(reversed(truck_weights))
    a = 1
    x = [[1],[t.pop()]]
    while x[1]:
        if x[0][0] == bridge_length:
            x[0].pop(0)
            x[1].pop(0)
        x[0] = [a+1 for a in x[0]]
        if t:
            if sum(x[1]) + t[-1] <= weight:
                x[0].append(1)
                x[1].append(t.pop())
        a += 1
    return a

# print(solution(1, 10, [1,1,1,1]))
# print(solution(5, 5, [2,2,2,2,1,1,1,1,1]))

# print(solution(2, 10, [7, 4, 5, 6]), 8)
# print(solution(100, 100, [10]), 101)
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)