# def solution(n):
#     v = 0
#     for i in range(n // 2 + 1):
#         m = n-2*i
#         t = 1
#         while i:
#             t *= (m+i)/i
#             i -= 1
#         v = (v + int(t)) % 1234567
#     return v

# 그냥 단순한 피보나치 문제
def solution(n):
    a = 1
    b = 1
    for i in range(n-1):
        c = b
        b += a
        a = c % 1234567
    return b % 1234567

# 222 1
# 2211 6
# 21111 5
# 111111 1
print(solution(6))
# 221 3
# 2111 4
# 11111 1
print(solution(5))
# print(solution(4))
# print(solution(3))
