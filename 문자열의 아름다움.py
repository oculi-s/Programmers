def solution(s):
    N = len(s)
    if s == s[0]*N:
        return 0
    else:
        V = [[j-i for j in range(N)] for i in range(N)]
        t = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[j] == s[i]:
                    V[i][j] = V[i][j-1]
            t += sum(V[i][i:])
        return t
    
print(solution('baby'))