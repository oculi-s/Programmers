def solution(files):
    a = [['@'], [''], ['']]
    b = ['@']
    while files:
        x = files.pop()
        for m in range(len(x)):
            if x[m].isdigit():
                n = m
                while x[n].isdigit():
                    n += 1
                    if n == len(x) or n == m + 5:
                        break
                break
        t = (x[:m], x[m:n], x[n:])
        if t[0].upper() in b:
            i = b.index(t[0].upper())
            while int(a[1][i]) < int(t[1]) and t[0].upper() == b[i]:
                i += 1
                if i == len(a[1]):
                    break
        else:
            i = 0
            while b[i] < t[0].upper():
                i += 1
                if i == len(b):
                    break
        a[0].insert(i, t[0])
        a[1].insert(i, t[1])
        if len(t) > 2:
            a[2].insert(i, t[2])
        b.insert(i, t[0].upper())
    b = []
    while a[0]:
        b.append(a[0].pop()+a[1].pop()+a[2].pop())
    return list(reversed(b))[1:]

print(solution(['f15','img00','f010bar020.zip','img000012345', 'img1.png','img2','IMG02']))
