def solution(p):
    if not p:
        return ''
    q = ''
    t = 0
    while p:
        q += p[0]
        t += q[-1] == '(' or -1
        p = p[1:]
        if not t:
            break
        g = t > 0
    if g:
        return q+solution(p)
    else:
        return '('+solution(p)+')' + ''.join(['('if x == ')' else ')' for x in q[1:-1]])

print(solution("(()())()"))
print('(()())()')
# print(solution("()))((()"))
