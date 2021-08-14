def solution(d):
    s = 0
    n = ''
    d = list(d)
    while d:
        x = d.pop(0)
        if x.isnumeric():
            n += x
        elif x in 'SDT':
            t = int(n)**' SDT'.index(x)
            if '*' in d:
                a = ''.join(d).split('*')[:-1]
                t *= 2 ** (a.count('') + any([x for x in a if x and len(x)<4]))
            if '#' in d:
                t *= (d[0] != '#') or -1
            s += t
            n = ''
    return s

            # print(x,s,t,a,d)
print(solution('1S1T1S*'))
print(solution('1D#2S*3S'))
print(solution('1S*10S*1S*'))
print(solution('1D2S#0T*'))
print(solution('1S2D*3T	'))