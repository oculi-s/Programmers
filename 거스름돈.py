def solution(n, money):
    a = 0
    while money:
        m = money.pop()
        a += not n % m
        if money:
            for d in range(m, n, m):
                a += solution(n - d, list(money))
    return a % 1000000007

def solution(n, money):
    t = money.pop(0)
    a = [not i % t for i in range(n+1)]
    
    for m in money:
        for i in range(m, n+1):
            a[i] += a[i-m]
    return a[n]

print(solution(5, [1, 2, 5]))
print(solution(20, [1, 2, 3, 4]), 108)
# print(solution(20, [2, 3]))


