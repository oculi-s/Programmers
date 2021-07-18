# def solution(A, B):
#     B.sort()
#     A.sort()
#     v = 0
#     while B:
#         x = B.pop()
#         i = 0
#         while i < len(A) and A[i] < x:
#             i += 1
#         if A[i-1] < x:
#             A.pop(i-1)
#             v += 1
#     return v

# def solution(A, B):
#     B.sort(reverse=True)
#     A.sort()
#     l = len(A)
#     for b in B:
#         for i in range(len(A)):
#             if A[i] > b:
#                 i -= 1
#                 break
#         if A[i] < b:
#             A.pop(i)
#     return l - len(A)

from bisect import bisect_left

def solution(A, B):
    B.sort(reverse=True)
    A.sort()
    for b in B:
        i = bisect_left(A,b)
        if i:
            A.pop(i-1)
    return len(B) - len(A)

print(solution([5,6,3,7],[2,2,6,8]))
# print(solution([5,9,3,7],[2,2,6,8]))
# print(solution([2,2,2,2],[1,1,1,1]))
# print(solution([2,2,2,2],[3,4,2,5]))