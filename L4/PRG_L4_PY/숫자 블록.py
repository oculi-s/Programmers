# def solution(begin, end):
#     a = [0] + [1] * (end-1)
#     for x in range(2,end//2+1):
#         for y in range(x*2-1,end,x):
#             a[y] = x
#         if x == 10000000:
#             break
#     return a[begin-1:]

# def solution(begin, end):
#     a = [0] + [1] * (end-1)
#     a = a[begin-1:]
#     for x in range(2, end//2+1):
#         for y in range(x*2-1, end, x):
#             a[y-begin+1] = x
#     return a

# def solution(begin, end):
#     a = [0] * (end-begin+1)
#     for x in range(1, end//2+1):
#         for y in range(x*2-1, end, x):
#             a[y-begin+1] = x
#     return a

from math import sqrt
def solution(begin, end):
    a = [1] * (end-begin+1)
    if begin == 1:
        a[0] = 0
    m = 10000000
    for i in range(begin, end+1):
        for t in range(2,int(sqrt(i))):
            if i//t <= m and not i % t:
                a[i-begin] = i//t
                break
    return a

# def solution(begin, end):
#     m = []
#     for x in range(1, end//2+1):
#         a = [0] * (2*x-1) + ([x]+[0]*(x-1)) * (end-2*x+1)
#         m.append(a[begin-1:end])
#     return [max(x) for x in list(zip(*m))]


# print(solution(1, 10))
# print(solution(11, 20))
print(solution(20000000,20000010))
# print(solution(100000001,100000001))
# print(solution(100000000,100000001))
