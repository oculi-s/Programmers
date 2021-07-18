# def solution(relation):
#     d = list(zip(*relation))
#     a = 0
#     x = d.pop(0)
#     while d:
#         print(d)
#         if len(set(x)) == len(x):
#             a += 1
#         else:
#             d.insert(0,list(zip(x,d.pop(0))))
#         x = d.pop(0)
#     return a

# from itertools import combinations
# def solution(relation):
#     d = list(zip(*relation))
#     a = []
#     for i in range(len(d)):
#         for x in combinations(d, i+1):
#             if len(set(list(zip(*x)))) == len(relation):
#                 if not any(set(y).issubset(set(x)) for y in a):
#                     a.append(x)
#     return len(a)

def solution(relation):
    c = [[]]
    for x in range(len(relation[0])):
        c += [y + [x] for y in c]
    c.remove([])
    a = []
    for x in c:
        if not any(set(y).issubset(set(x)) for y in a):
            t = [tuple(y[c] for c in x) for y in relation]
            if len(set(t)) == len(relation):
                a.append(x)
    return len(a)

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
# print(solution([["200", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
# print(solution([['a','1','4'],['2','1','5'],['a','2','4']]))
# print(solution([['a','b','c'],['1','b','c'],['a','b','4'],['a','5','c']]))
# print(solution([['a','1','4'],['2','1','5'],['a','2','4']]))
# print(solution([["a","aa"],["aa","a"],["a","a"]]))
# print(solution([["a"],["b"],["c"]]))
# print(solution([["ab", "c"], ["a", "bc"], ["x", "yz"], ["x", "c"]]))
# print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))
