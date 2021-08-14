# def solution(numbers):
#     a = ''
#     n = [str(x) for x in numbers]
#     m = '0'
#     while n:
#         for x in n:
#             t = a + x
#             print(t,m)
#             if int(t[:len(m)]) >= int(m[:len(t)]):
#                 m = t
#                 tx = x
#         a = m
#         n.remove(tx)
#     return a

# def solution(numbers):
#     n = dict(enumerate(sorted(str(x) for x in numbers)))
#     s = []

#     for i in range(len(n)):
#         j = i
#         while n[i][0] == n[j][0]:
#             j += 1
#             if j >= len(n):
#                 break
#         t = []
#         if n[i][0] not in s and j > i + 1:
#             s.append(n[i][0])
#             for k in range(i,j):
#                 if len(n[k]) == 1:
#                     n[k] *= 2
#                     t.append(k)
#             l = enumerate(sorted(list(n.items())[i:j],key=lambda c:c[1]))
#             for x in l:
#                 if x[1][0] in t:
#                     n[x[0]] = x[1][1][0]
#                 else:
#                     n[x[0]] = x[1][1]
#     return str(int(''.join(list(reversed(n.values())))))

# from itertools import permutations
# def solution(numbers):
#     n = sorted(str(x) for x in numbers)
#     s = ''
#     while n:
#         x = n.pop()
#         if not n:
#             s += x
#             break
#         if x[0] not in n[-1]:
#             s += x
#         else:
#             g = [x]
#             while x[0] in n[-1]:
#                 g.append(n.pop())
#                 if not n:
#                     break
#             s += max(''.join(x) for x in permutations(g))
#     return str(int(s))

def solution(numbers):
    n = sorted(str(x) for x in numbers)
    s = ''
    while n:
        x = n.pop()
        if not n:
            s += x
            break
        if x[0] not in n[-1]:
            s += x
        else:
            g = [x]
            while x[0] in n[-1]:
                g.append(n.pop())
                if not n:
                    break
            t = sorted([[x*4,x] for x in g],key=lambda c:c[0],reverse=True)
            s += ''.join(list(zip(*t))[1])
    return str(int(s))

def solution(numbers):
    n = sorted(str(x) for x in numbers)
    n = sorted([[x*4,x] for x in n],key=lambda c:c[0],reverse=True)
    return str(int(''.join(list(zip(*n))[1])))

# 9534330
# print(solution([6,10,2]))
# print(solution([30, 34, 9, 3, 5]))
# print(solution([15,151,151,1512]))
# print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(solution([0, 5, 10, 15, 20]))
# print(solution([1000, 0, 5, 99, 100]))
# print(solution([0,0,0,0,0]))
print(solution( [89,898,8] ))
print(solution( [9,90,908] ))
# print(solution( [908,9,9088,908] ))
# print(solution( [90,908,89,898,10,101,1,8,9] ))
# print(''.join(str(x) for x in [9, 90, 908, 89, 898, 8, 1, 101, 10]))
#987654321101000