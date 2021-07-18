def solution(n, results):
    w = {x:set() for x in range(n)}
    l = {x:set() for x in range(n)}
    for x, y in results:
        w[x-1].add(y-1)
        l[y-1].add(x-1)
    for _ in range(n):
        for x in w:
            t = list(w[x])
            for y in t:
                w[x].update(w[y])
            t = list(l[x])
            for y in t:
                l[x].update(l[y])
    return sum(len(w[x]|l[x]) == n-1 for x in w)

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
print(solution(3, [[1,2],[1,3]]), 1)
print(solution(6, [[1,6],[2,6],[3,6],[4,6]]), 0)
print(solution(8, [[1,2],[3,4],[5,6],[7,8]]),0)
print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]]), 1)
print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]]), 4)
print(solution(3,[[3,2],[3,1]]), 1)
print(solution(4, [[1,2],[1,3],[3,4]]), 1)