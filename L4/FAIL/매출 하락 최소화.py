# from itertools import product
# def solution(sales, links):
#     g = {x:[x] for x in sorted(list(zip(*links))[0])}
#     for x in links:
#         g[x[0]].append(x[1])
#     v = set()
#     for x in product(*g.values()):
#         v.add(sum(sales[y-1] for y in set(x)))
#     return min(v)

def solution(sales, links):
    sales = [0] + sales
    d = sorted(set(list(zip(*links))[0]))
    g = {x:[] for x in d}
    r = {x:[] for x in d}
    for x in links:
        if sales[x[0]] > sales[x[1]] or x[0] in d:
            g[x[0]].append(x[1])
        if x[1] in d:
            r[x[0]].append(x[1])
    k = []
    s = 1
    for x in r[s]:
        
    print(r)
    print(g)

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
# print(solution([5, 6, 5, 3, 4],[[2,3], [1,4], [2,5], [1,2]]))
# print(solution([5, 6, 5, 1, 4],[[2,3], [1,4], [2,5], [1,2]]))
# print(solution([10, 10, 1, 1],[[3,2], [4,3], [1,4]]))