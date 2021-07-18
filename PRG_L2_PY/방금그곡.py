def solution(m, musicinfos):
    ht = 0
    a = "(None)"
    for x in musicinfos:
        x = x.split(',')
        x[0] = x[0].split(':')
        x[1] = x[1].split(':')
        t = [int(y)-int(x) for x, y in zip(*x[0:2])]
        t = t[0] * 60 + t[1]
        l = (t//len(x[3].replace('#', '')) + 1) * x[3]
        while t != len(l.replace('#','')):
            l = l[:-1]
        if m in l.replace(m+'#', ''):
            if t > ht:
                a = x[2]
                ht = t
    return a

# print(solution(	"ABCDEFG", ["12:50,12:52,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABC#DEF"]))
# print(solution(	"ABCDEFG", ["23:50,24:52,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABC#DEF"]))
print(solution('CCB',["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))
# print(solution(	"CC#BCC#BCC#BCC#B", [
#       "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(
#     solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
