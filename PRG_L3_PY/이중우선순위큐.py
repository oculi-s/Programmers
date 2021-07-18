def solution(operations):
    s = []
    for x in operations:
        a, b = x.split()
        b = int(b)
        if a == 'I':
            i = 0
            for i in range(len(s)):
                if s[i] > b:
                    i -= 1
                    break
            s.insert(i+1, b)
        elif s:
            if b == 1:
                s.pop()
            else:
                s.pop(0)
    if not s:
        return [0, 0]
    return [max(s), min(s)]


# print(solution(["I 16", "D 1"]))
# print(solution(["I 7", "I 5", "I -5", "D -1"]))
# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
# print(solution(["D 1", 'D 1','D 1']))
# print(solution(["I 16"]))
print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))
