def solution(left, right):
    v = -2*(left == 1)
    for i in range(left,right+1):
        t = 1
        for j in range(2,i):
            t += not(i % j)
        v += (t % 2 or -1) * i
        print(i,t)
    return v

print(solution(1,10))