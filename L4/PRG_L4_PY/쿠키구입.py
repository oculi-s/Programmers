# def solution(cookie):
#     R = len(cookie)
#     l, m, r = 0, 1, 2
#     a, b, c = cookie[0]+cookie[1], cookie[2], 0
#     while l < R-2:
#         if a == b:
#             c = a
#         if a > b:
#             while r < R-1:
#                 r += 1
#                 b += cookie[r]
#                 if a <= b:
#                     break
#             if a == b:
#                 c = a
#         if m < R-2:
#             m, r = m+1, m+2
#             a += cookie[m]
#             b = cookie[r]
#         if m == R-2:
#             l, m, r = l+1, l+2, l+3
#             if l < R-2:
#                 a, b = cookie[l]+cookie[m], cookie[r]
#     return c

# # 전체 합의 절반과 같으면
# def solution(cookie):
#     R = len(cookie)
#     l, m, r = 0, (0+R)//2, R
#     S = sum(cookie[l:r])//2
#     L = sum(cookie[l:m])
#     tl, tr = l, r
#     print(L,S, l,m,r,tl,tr)
#     while l < r-1:
#         if L == S:
#             return S
#         else:
#             if L > S:
#                 tr = m
#                 m = (tl+tr)//2
#                 L -= sum(cookie[m:tr])
#             elif L < S:
#                 tl = m
#                 m = (tl+tr)//2
#                 L += sum(cookie[tl:m])
#             if abs(L - S) < cookie[m-1]:
#                 l += 1
#                 m = (l+r)//2
#                 S = sum(cookie[l:r])//2
#                 L = sum(cookie[l:m])


# def solution(cookie):
#     R = len(cookie)
#     l, r = -1, R
#     b = sum(cookie)
#     while l < R-2:
#         l, m = l+1, R-1
#         a = b-cookie[r-1]
#         if b % 2 == 0:
#             if a == b//2:
#                 return a
#             elif a > b//2:
#                 while m > l:
#                     m -= 1
#                     a -= cookie[m]
#                     if a <= b//2:
#                         break
#                 if a == b//2:
#                     return a
#         b -= cookie[l]

#     l, r = 0, R+1
#     b = sum(cookie)
#     while r > 2:
#         r, m = r-1, r-2
#         a = b-cookie[r-1]
#         if b % 2 == 0:
#             if a == b//2:
#                 return a
#             elif a > b//2:
#                 while m > l:
#                     m -= 1
#                     a -= cookie[m]
#                     if a <= b//2:
#                         break
#                 if a == b//2:
#                     return a
#         b -= cookie[r-1]
#     return 0


# def solution(cookie):
#     r = len(cookie)
#     A = 0
#     while r > 1:
#         l = -1
#         b = sum(cookie[:r])
#         while l < r-2:
#             l, m = l+1, (r+l+1)//2
#             a = b-sum(cookie[m:r])
#             if b % 2 == 0:
#                 if a == b//2:
#                     A = max(A, a)
#                 elif a > b//2:
#                     while m > l:
#                         m -= 1
#                         a -= cookie[m]
#                         if a <= b//2:
#                             break
#                     if a == b//2:
#                         A = max(A, a)
#                 elif a < b//2:
#                     while m < r:
#                         m += 1
#                         a += cookie[m]
#                         if a >= b//2:
#                             break
#                     if a == b//2:
#                         A = max(A, a)
#             b -= cookie[l]
#         r -= 1
#     return A

# def solution(cookie):
#     r = len(cookie)
#     A = 0
#     while r > 1:
#         l = -1
#         b = sum(cookie[:r])
#         while l < r-2:
#             l, m = l+1, r-1
#             a = b-cookie[r-1]
#             if b % 2 == 0:
#                 if a == b//2:
#                     A = max(A, a)
#                 elif a > b//2:
#                     while m > l:
#                         m -= 1
#                         a -= cookie[m]
#                         if a <= b//2:
#                             break
#                     if a == b//2:
#                         A = max(A, a)
#             b -= cookie[l]
#         r -= 1
#     return A

def solution(cookie):
    S, L = [0]+cookie, 1+len(cookie)
    for i in range(L-1):
        S[i+1] += S[i]
    A, B = 0, sum(cookie)
    for l in range(L-2):
        if B//2 > A:
            for m in range(l+1, L-1):
                t = S[m]-S[l]
                if t > A:
                    for r in range(m+1, L):
                        if S[r]-S[m] >= t:
                            if S[r]-S[m] == t:
                                A = max(A, t)
                            break
        B -= cookie[l]
    return A

print(solution([1, 1, 2, 3]), 3)
print(solution([1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]), 15)
print(solution([1, 2, 4, 4, 9]), 4)
print(solution([1, 2, 2, 2, 2, 9]), 9)
# print(solution([1, 2, 4, 5]), 0)
