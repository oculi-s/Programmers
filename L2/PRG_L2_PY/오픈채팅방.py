def solution(record):
    d = {}
    a = ''
    s = ['/님이 들어왔습니다.//','/님이 나갔습니다.//']
    for x in record:
        x = x.split(' ')
        if x[0][0] in 'EL':
            i = 'EL'.index(x[0][0])
            a += x[1] + s[i]
        if len(x) == 3:
            d[x[1]] = x[2]
    b = []
    for x in a.split('//')[:-1]:
        x = x.split('/')
        b.append(d[x[0]]+x[1])
    return b

print(solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
print(solution(["Enter a b", "Enter b c", "Leave b", "Enter c b", "Change c d"]))