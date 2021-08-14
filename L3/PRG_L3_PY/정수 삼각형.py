# def solution(triangle):
#     s = len(triangle)
#     f = 1
#     n = s
#     while n > 1:
#         f *= n
#         n -= 1
#     n = f
#     for i in range(s):
#         f //= (i + 1)
#         t = [triangle[i]] * f
#         t = [list(x) for x in zip(*t)]
#         triangle[i] = sum(t*(n//f//(i+1)), [])
#     m = 0
#     for x in zip(*triangle):
#         if sum(x) > m:
#             m = sum(x)
#     return m

def solution(triangle):
    while len(triangle) > 1:
        x = triangle.pop()
        for i in range(len(x)-1):
            triangle[-1][i] += max(x[i:i+2])
    return triangle[0][0]        

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))