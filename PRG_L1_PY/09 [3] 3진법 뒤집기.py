def solution(n):
    n3 = []
    while n >= 1:
        n3.insert(0,n%3)
        n = int(n/3)
    return sum([n3[i]*3**i for i in range(len(n3))])
print(solution(125))