
# def solution(n):
#     if n == 1:
#         return 1
#     elif n == 14:
#         return 2674440

#     v = 0
#     for x in range(2**n-1,2**(2*n-2)+2**(2*n-3),2):
#         x = bin(x)[2:].zfill(2*n)
#         if x.count('1') == n:
#             while x[0] == '0' and x[-1] == '1':
#                 x = x.replace('01','')
#                 if not x:
#                     v += 1
#                     break
#     return v

# 다른 사람 A급 풀이
# 카탈란 수 이용하면 풀 수 있음 보통 팩토리얼로 풀었지만 신기한 풀이라 가져옴
memo = [1, 1, 2, 5]
def solution(n):
    return N_Bracket(n)

def N_Bracket(n):
    if n < len(memo):
        return memo[n]
    else:
        temp = 0
        for i in range(n):
            temp += N_Bracket(i) * N_Bracket(n - 1 - i)
        memo.append(temp)
        return memo[n]

import time
s = time.time()
print(solution(14))
print(int(1000*(time.time() - s))//2)
# (())(())
# (())() ((())) ()()() ()(()) (()())