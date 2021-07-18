# def solution(s):
#     s = list(s)
#     i = 0
#     while len(s) > 1:
#         if s[i] == s[i+1]:
#             del s[i:i+2]
#             i = 0
#         else:
#             i += 1
#     return 0

# a = "abcdefghijklmnopqrstuvwxyz"
# def solution(s):
#     while s:
#         a = list("abcdefghijklmnopqrstuvwxyz")
#         x = a.pop()
#         while x*2 not in s:
#             a = [x] + a
#             x = a.pop()
#             if x == 'z':
#                 return 0
#         s = s.replace(x*2,'')
#     return int(not s)

# def solution(s):
#     if s:
#         a = set(s)
#         while a:
#             x = a.pop()
#             if x*2 in s:
#                 return solution(s.replace(x*2,''))
#         return 0
#     else:
#         return 1

# def solution(s):
#     ts = s
#     while s:
#         a = set(s)
#         for x in a:
#             s = s.replace(x*2,'')
#         if s == ts:
#             return 0
#         ts = s
#     return 1

# def solution(s):
#     s = list(s)
#     t = list(s)
#     while len(s) > 1:
#         print(s)
#         x = s.pop()
#         y = s.pop()
#         if y != x:
#             s.insert(0, x)
#             s.append(y)
#             continue
#         s = s.replace(x*2)
#     return int(not s)

# def solution(s):
#     s = list(s)
#     t = list(s)
#     while True:
#         x = s.pop()
#         y = s.pop()
#         if y != x:
#             s.insert(0, x)
#             s.append(y)
#             if s == t:
#                 return 0
#         elif len(s) < 2:
#             return int(not s)

# def solution(s):
#     s = list(s)
#     t = list(s)
#     while len(s) > 1:
#         if s[-1] == s[-2]:
#             s.pop()
#             s.pop()
#         else:
#             s[0:0] = s.pop()
#             if s == t:
#                 return 0
#     return int(not s)

# def solution(s):
#     t = s[1:]+s[0]
#     while s != t:
#         s = s.replace(s[-1]*2,'')
#         if len(s) in [0,1]:
#             return 1 - len(s)
#         if s[-1] != s[-2]:
#             s = s[-1]+s[:-1]
#     return 0

# def solution(s):
#     t = s[-1]+s[:-1]
#     while s:
#         s = s[1:]+s[0]
#         if s == t or len(s) == 1:
#             return 0
#         elif s[0] == s[1]:
#             s = s[2:]
#     return int(not len(s))

# def solution(s):
#     t = str(s)
#     for x in set(s):
#         s = s.replace(x*2,'')
#     if not s:
#         return 1
#     elif s == t:
#         return 0

#     d = {x:s.count(x)%2 for x in set(s)}
#     e = [s[i] == s[i+1] for i in range(len(s)-1)]
#     if sum(e) == 0 or any(d.values()):
#         return 0
    
#     s = list(s)
#     while s:
#         x = s.pop()
#         if s:
#             if s[-1] != x:
#                 s[0:0] = x
#             else:
#                 s.pop()
#     return 1

def solution(s):
    w = 'abcdefghijklmnopqrstuvwxyz'
    for x in w:
        if s.count(x) % 2:
            return 0
    a = ['']
    s = list(s)
    for i in range(len(s)):
        if s[i] == a[-1]:
            a.pop()
            continue
        a.append(s[i])
        if len(s)-i < len(a)-1:
            return 0
    return 1

print(solution("cdcd"))
# print(solution("baabaa"))
# print(solution("abccaabaa"))
# print(solution("abccccbaaa"))
# print(solution("abcccba"))
# print(solution("abccaabaa"))

# from random import randint
# from time import time

# s = ''
# a = 'abc'
# t = time()
# for i in range(1000):
#     s += a[randint(0,len(a)-1)]
# print(time()-t)

# t = time()
# print(solution(s))
# print(time()-t)
# print(solution(randint(10)))
