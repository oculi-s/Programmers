def solution(matrix_sizes):
    a = matrix_sizes.pop(0)
    a += [m[1] for m in matrix_sizes]

    s = [[0, a]]
    while len(s[0][1]) > 3:
        t = []
        for v, x in s:
            for i in range(1, len(x)-1):
                y = x[:i] + x[i+1:]
                t.append([v + x[i-1] * x[i] * x[i+1], y])
        s = t
    v = [v+x[0] * x[1] * x[2] for v, x in s]
    return min(v)

# DP 로 풀 수 있는 문제?

def solution(matrix_sizes):
    S = matrix_sizes.pop(0)
    S += [m[1] for m in matrix_sizes]
    v = 0
    while len(S) > 2:
        i = S.index(max(S[1:-1]))
        v += S[i-1]*S[i]*S[i+1]
        S.pop(i)
    return v

print(solution([[5, 3], [3, 10], [10, 6]]))
print(solution([[5,3],[3,10],[10,6],[6,2],[2,4]]))
