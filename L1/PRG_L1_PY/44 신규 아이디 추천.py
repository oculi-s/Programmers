def solution(new_id):
    a = ''.join(x for x in new_id.lower() if x in 'abcdefghijklmnopqrstuvwxyz0123456789-_.')
    for x in reversed(range(2,15)):
        a = a.replace('.'*x,'.')
    if a:
        if a[0] == '.':
            a = a[1:]
        if a:
            if a[-1] == '.':
                a = a[:-1]
        if a:
            a = a[:15]
            if a[-1] == '.':
                a = a[:-1]
    a = a or 'a'
    if len(a) < 3:
        a = (a + a[-1]*3)[:3]
    return a


print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution('=.='))
# print(solution("z-+.^."))
# print(solution("abcdefghijklmn.p"))
