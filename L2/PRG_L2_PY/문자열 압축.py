def solution(s):
    l = len(s)
    a = len(s)
    for x in range(1,l):
        b = len(s)
        t = ''
        c = 1
        for i in range(0,l,x):
            if s[i:i+x] == t:
                b -= x
                c += 1
            elif c != 1:
                b += len(str(c))
                c = 1
            t = s[i:i+x]
        if c != 1:
            b += len(str(c))
        if b < a:
            a = b
    return a