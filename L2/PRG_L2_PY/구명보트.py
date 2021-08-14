from time import time

# def solution(people, limit):
#     p = sorted(people, reverse=True)
#     a = len(p)
#     i = 0
#     while p and p[-1] <= limit/2:
#         x = p.pop()
#         for i in range(i,len(p)):
#             if x + p[i] <= limit:
#                 p.pop(i)
#                 a -= 1
#                 break
#     return a

# def solution(people, limit):
#     p = sorted(people, reverse=True)
#     a = len(p)
#     i = 0
#     x = p.pop()
#     while p:
#         if x + p[-1] > limit:
#             return a
#         else:
#             while i < len(p):
#                 if x + p[i] <= limit:
#                     p.pop(i)
#                     a -= 1
#                     break
#                 i += 1
#             x = p.pop()
#     return a

# def solution(people, limit):
#     p = sorted(people, reverse=True)
#     a = len(p)
#     i = 0
#     x = p.pop()
#     while True:
#         while p and x <= limit / 2 and i < len(p):
#             if x + p[i] <= limit:
#                 p.pop(i)
#                 a -= 1
#                 break
#             i += 1
#         x = p.pop()
#         return a

# def solution(people, limit):
#     p = sorted(people, reverse=True)
#     a = len(p)
#     i = 0
#     while p[-1] <= limit/2:
#         x = p.pop()
#         while p:
#             if x + p.pop(0) <= limit:
#                 a -= 1
#                 break
#         if not p:
#             return a
#     return a

# def solution(people, limit):
#     p = sorted(people, reverse=True)
#     a = len(p)
#     j = 0
#     for i in reversed(range(a)):
#         for j in range(j,i):
#             if p[i] + p[j] <= limit:
#                 del p[j]
#                 a -= 1
#                 break
#     return a

# def solution(people, limit):
#     p = sorted(people)
#     a = len(p)
#     i = 0
#     while i < len(p):
#         x = p.pop(0)
#         while p:
#             if x + p.pop(i) <= limit:
#                 a -= 1
#                 break
#     return a

# def solution(people, limit):
#     p = sorted(people,reverse = True)
#     a = 1
#     while p:
#         x = p.pop()
#         while x + p.pop(0) > limit:
#             a += 1
#             print(p,x)
#             if not p:
#                 break
#     return a

# def solution(people, limit):
#     p = sorted(people,reverse = True)
#     l = len(p)
#     i = 0
#     while l:
#         l -= 1
#         x = p[l]
#         while i < l:
#             if x + p[i] <= limit:
#                 p.pop(i)
#                 l -= 1
#                 break
#             i += 1
#     return len(p)

# def solution(people, limit):
#     p = sorted(people, reverse=True)
#     a = len(p)
#     x = limit - p[-1]
#     for i in range(a):
#         if i == len(p):
#             return a
#         elif p[i] > x:
#             break
#     while p and p[-1] <= limit/2:
#         x = p.pop()
#         for i in range(i,len(p)):
#             if x + p[i] <= limit:
#                 p.pop(i)
#                 a -= 1
#                 break
#     return a

def solution(people, limit):
    p = sorted(people)
    i = 0
    a = 0
    while i < len(p):
        if p[i] + p.pop() <= limit:
            i += 1
        a += 1
    return a

# print(solution([40, 40, 40], 100))
# print(solution([40, 50, 60, 90], 100))
# print(solution([70, 50, 80, 50], 100))

t = time()
for i in range(10):
    solution([70,50,80,50]*200,100)
print(time()-t)
t = time()
for i in range(1000):
    solution([70,50,80,50],100)
print(time()-t)
