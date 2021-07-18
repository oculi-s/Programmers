def solution(name):
    a = 0
    s1 = "_BCDEFGHIJKLM"
    s2 = "_ZYXWVUTSRQPON"
    for x in name:
        if x in s1:
            a += s1.index(x)
        elif x in s2:
            a += s2.index(x)

    i = 0
    t = len(name)
    for i in range(t):
        j = i
        while name[j:].replace('A', ''):
            j += 1
        if i + 2 * (j - i - 1) < t:
            t = i + 2 * (j - i - 1)
        print(i,j,t,name)
        name = name[-1] + name[:-1]
    return a + t