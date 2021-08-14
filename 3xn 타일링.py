def solution(n):
    if n < 2:
        return 0
    elif n == 2:
        return 3
    else:
        a = 2
        for i in range(1,n//2):
            a += (solution(2*i)-solution(2*i-2)) * (solution(n-2*i)-solution(n-2*i-2))
        return a

import sys
sys.setrecursionlimit(1000)

def solution(n):
    if n < 5:
        return [1, 3, 11][n//2]
    else:
        s = 2+3*solution(n-2)
        for i in range(0,n-2,2):
            s += 2*solution(i)
        return s%1000000007


def solution(n):
    a, b, r = 1, 3, 1000000007
    for _ in range(n//2):
        a, b = b, (4*b-a) % r
    return a

# 4개에는 2가지방법, 2개에는 3가지 방법
# 4는 4하나 2가지방법
# 2두개 9가지

# 6
# 2개, 3**(n//2)개는 고정
# 9*2
# 27, 18, 2


print(solution(4))
print(solution(6))
print(solution(8))
print(solution(10))

#8
# 1111 121 211 112 13 31 22 4
# (81) (9*2)*3 (3*2)*2 (4)*1 2
# 153


# 10

# 11111
# 1112 1121 1211 2111
# 113 131 311 221 212 122
# 14 41 23 32
# 5

# 243
# (27*2)*4 = 216
# (9*2)*3+(3*4)*3 = 90
# (3*2)*2+(2*2)*2 = 20
# 2*1 = 2
# 571
