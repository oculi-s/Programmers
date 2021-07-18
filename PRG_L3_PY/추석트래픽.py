def solution(lines):
    a = []
    for x in lines:
        x,d = x.split()[1:]
        h,m,s = x.split(':')
        x = int(1000*(int(h)*3600+int(m)*60+float(s)))
        a.append([x-int(1000*float(d[:-1]))+1,x])
    a.sort()
    s = list(zip(*a))[0]
    b = []
    for x in a:
        t = 0
        for y in a:
            if y[0] < x[1]+1000:
                if x[1] <= y[1]:
                    t += 1
        b.append(t)
    return max(b)