def solution(s):
    a = []
    for x in s[1:-1].split('},{'):
        a.append(set(x.replace('{','').replace('}','').split(',')))
    d = {len(x):x for x in a}
    for i in range(1,len(a)+1):
        for j in range(i+1,len(a)+1):
            d[j] -= d[i]
    return [int(d[x].pop()) for x in sorted(d)]

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))