from bisect import bisect
def solution(strs, t):
    strs.sort()
    r = [[0, ""]]
    while r:
        v, x = r.pop(0)
        if x == t:
            return v
        i, j = 0, len(strs)
        if len(x) < len(t):
            i = bisect(strs, t[len(x)])
            j = bisect(strs, chr(ord(t[len(x)])+1))
        for y in strs[i:j]:
            r.append([v+1, x+y])
        print(r)
    return -1

def solution(strs, t):
    strs.sort()
    r = [[0, ""]]
    while r:
        v, x = r.pop(0)
        if x == t:
            return v
        for y in strs:
            if t[len(x)] == y[0]:
                r.append([v+1, x+y])
    return -1

def solution(strs, t):
    r = [[0, ""]]
    while r:
        v, x = r.pop(0)
        if x == t:
            return v
        elif x > t:
            return -1
        for y in strs:
            if t[len(x)] == y[0]:
                r.append([v+1, x+y])
    return -1

# print(solution(["ba", "na", "n", "a"], "banana"))
# print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], 'apple'))
print(solution(["ba", "an", "nan", "ban", "n"], 'banana'))
# print("ba"<"b")
