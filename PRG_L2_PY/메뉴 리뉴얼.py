def comb(s,t,self,n,r):
    if r == 0:
        if s != ''.join(t):
            self.append(''.join(t))
    elif n >= r:
        t[r-1] = s[n-1]
        comb(s,t,self,n-1,r-1)
        comb(s,t,self,n-1,r)

def solution(orders, course):
    t = [set(x) for x in orders]
    d = set()
    while t:
        x = t.pop()
        for y in t:
            s = ''.join(sorted(x & y))
            if len(s) > 1:
                d.add(s)
                if len(s) > min(course):
                    for c in course:
                        tl = []
                        tx = ['0']*c
                        comb(s,tx,tl,len(s),c)
                        for z in tl:
                            d.add(z)
    a = {}
    b = {}
    for x in d:
        a[x] = sum(set(x).issubset(set(y)) for y in orders)
        l = len(x)
        if l not in b or a[x] > b[l]:
            b[l] = a[x]
    for x in d:
        l = len(x)
        if l not in course or a[x] < b[l]:
            a.pop(x)
    return sorted(a)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))
print(solution(	["ABCDEFGHIK", "ABCDEFGHIJ"], [9, 10]))