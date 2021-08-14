def solution(numbers):
    m = int(''.join(sorted(numbers,reverse=True)))
    d = {str(x):numbers.count(str(x)) for x in range(10)}
    n = 0
    for i in range(2,m+1):
        i = str(i)
        if not any(i.count(x) > d[x] for x in i):
            i = int(i)
            if not any(not i % j for j in range(2,i)):
                n += 1
    return n

print(solution("17"))