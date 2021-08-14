def solution(progresses, speeds):
    a = [(100-x)/y for x,y in zip(progresses,speeds)]
    print(a)
    a = list(reversed([(not not x%1) + x - x%1 for x in a]))
    print(a)
    b = []
    while(a):
        x = a.pop()
        t = 1
        for _ in a:
            y = a.pop()
            if y <= x:
                t += 1
            else:
                a.append(y)
                break
        b.append(t)
    return b

p = [5, 5, 5]
s = [21,25,20]
print(solution(p,s))