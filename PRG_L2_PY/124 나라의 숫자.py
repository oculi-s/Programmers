def solution(n):
    a = '412'[n % 3]
    while(n > 3):
        n = (n-1)//3
        a = '412'[n % 3] + a
    return a


for i in range(1, 11):
    print(solution(i))
