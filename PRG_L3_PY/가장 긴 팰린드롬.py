def solution(s):
    L = len(s)
    for l in range(L):
        for i in range(l+1):
            x = s[i:L-l+i]
            if x[:(L-l)//2] == x[:(L-l-1)//2:-1]:
                return L-l

print(solution('abcdcba'))
print(solution('abacde'))