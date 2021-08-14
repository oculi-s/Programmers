def solution(msg):
    a = []
    msg += '_'
    s = list('_ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while len(msg) > 1:
        i = 0
        while msg[:-i] not in s:
            i += 1
        a += [s.index(msg[:-i])]
        s += [msg[:-i+1]]
        msg = msg[-i:]
    return a