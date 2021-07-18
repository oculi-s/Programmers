def solution(n):
    s = [[[0]*n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        s[i][0][i] = 1
    for m in s:
        for i in range(n):
            if m[0][i]:
                for j in range(1,n):
                    m[j][i] = -1
                    if i-(j-i) < n:
                        m[j][i-(j-i)] = -1
                    if i+(j-i) > -1:
                        m[j][i+(j-i)] = -1
    for x in s:
        for y in x:
            print(y)
        print()
    return 1

print(solution(4))