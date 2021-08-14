def solution(expression):
    d = set(expression) - set('1234567890')
    n = expression
    for x in d:
        n = n.replace(x,' '+x+' ')
    n = n.split(' ')
    
    if len(d) == 3:
        c = ['012','021','102','120','201','210']
    elif len(d) == 2:
        c = ['01','10']
    else:
        c = ['0']
    m = 0
    for c in c:
        a = {int(x):y for x,y in zip(c,d)}
        b = list(n)
        for i in range(len(d)):
            j = 1
            while a[i] in b:
                if b[j] == a[i]:
                    x = int(b.pop(j+1))
                    b.pop(j)
                    if a[i] == '*':
                        x *= int(b.pop(j-1))
                    elif a[i] == '+':
                        x += int(b.pop(j-1))
                    elif a[i] == '-':
                        x = int(b.pop(j-1)) - x
                    b.insert(j-1,str(x))
                    j = -1
                j += 2
        if abs(x) > m:
            m = abs(x)
    return m

# print(solution("100-200*300-500+20"	))
# print(solution("50*6-3*2"))
print(solution("50*6"))