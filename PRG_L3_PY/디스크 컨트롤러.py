def solution(jobs):
    jobs.sort(key= lambda c:c[0])
    jobs.sort(key= lambda c:c[1])
    a, v = 0, jobs[0][0]
    for x, y in jobs:
        a += v+y-x
        v += y
    return a//len(jobs)


# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[0, 3], [1, 9],[1,6],[0,9], [2, 6]]))
# print(solution([[0, 1], [0, 2], [0, 3], [0, 4]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
