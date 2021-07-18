from bisect import bisect_right
def solution(n, t, m, timetable):
    s = [x.split(':') for x in timetable]
    s = sorted(int(x[0])*60+int(x[1]) for x in s)
    v = 540
    l = bisect_right(s, v)
    if l >= n*m:
        v = s[n*m-1] - 1
    else:
        while n:
            # l = 몇명을 보낼 것인가
            l = min(l,m)
            print(l,n,m,s)
            if l >= n*m:
                if s:
                    v = min(v, s[0])
                    print(v,s,n,m)
                    break
            s = s[l:]
            n -= 1
            v += t
            l = bisect_right(s, v)
    m, s = v//60, v % 60
    return str(m).zfill(2)+':'+str(s).zfill(2)

print(solution(2,10,2,["09:10", "09:09", "08:00"]))