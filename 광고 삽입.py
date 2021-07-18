def f(s):
    s = s.split(':')
    return int(s[0])*3600+int(s[1])*60+int(s[2])

from bisect import bisect
def solution(play_time, adv_time, logs):
    logs.sort()
    p, a = play_time.split(':'), adv_time.split(':')
    p = int(p[0])*3600+int(p[1])*60+int(p[2])
    a = int(a[0])*3600+int(a[1])*60+int(a[2])
    S, E = [], []
    for x in logs:
        t = x.replace('-',':').split(':')
        S.append(int(t[0])*3600+int(t[1])*60+int(t[2]))
        E.append(int(t[3])*3600+int(t[4])*60+int(t[5]))
    M, MT = 0, 0
    for s in S:
        if s + a > p:
            break
        i, j = bisect(E, s-a), bisect(S, s+a)
        v = 0
        for x, y in zip(S[i:j],E[i:j]):
            v += min(a, y-s, s+a-x)
        print(i,j,g(v))
        if M < v:
            MT = S.index(s)
            M = v
    return logs[MT].split('-')[0]

def g(s):
    return str(s//3600).zfill(2)+':'+str(s % 3600//60).zfill(2)+':'+str(s % 60).zfill(2)

# def f(a,b,x):
#     a = a.split(':')
#     b = b.split(':')
#     s = int(a[0])*3600+int(a[1])*60+int(a[2])
#     s += x * int(b[0])*3600+int(b[1])*60+int(b[2])
#     return str(s//3600).zfill(2)+':'+str(s % 3600//60).zfill(2)+':'+str(s % 60).zfill(2)

# from bisect import bisect
# def solution(play_time, adv_time, logs):
#     logs.sort()
#     logs = [x.split('-') for x in logs]
#     M, MT = '00:00:00', '00:00:00'
#     S, E = zip(*logs)
#     for s, e in logs:
#         if f(s, adv_time, 1) > play_time:
#             break
#         i, j = bisect(E,s), bisect(S,f(s, adv_time, 1))
#         v = '00:00:00'
#         for x, y in logs[i:j]:
#             v = f(v,min(adv_time, f(y, s, -1)),1)
#             print(v)
#         if M < v:
#             M, MT = v, s
#         print(s,e,v)
#     return MT

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
