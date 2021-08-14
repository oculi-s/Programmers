def solution(n, t, m, p):
    a = '0'
    b = list('0123456789ABCDEF')
    x = 1
    while True:
        y = x
        s = ''
        while y:
            s = b[y % n] + s
            y //= n
        x += 1
        a += s
        if len(a) > m*t:
            return a[p-1:m*t:m]