# def solution(tickets):
#     t = list(set(sum(tickets,[])))
#     t.remove('ICN')
#     t = ['ICN'] + t

#     g = {x:[] for x in t}
#     for x in tickets:
#         g[x[0]].append(x[1])
#     h = None
#     for x in g:
#         if not g[x]:
#             h = x
    
#     s = ['ICN']
#     tn = 'ICN'
#     v = []
#     while s:
#         n = s.pop()
#         print(n,v,s)
#         if g[n]:
#             v.append(n)
#             s += sorted(g[n],reverse=True)
#         elif s:
#             s.append(n)
#             print(n,v,s,g[n])
#             while not g[n]:
#                 print(n,v,s)
#                 n = v.pop()
#                 s.append(n)
#             n = s.pop(0)
#         tn = n
#     return v + [h or n]

def solution(tickets):
    t = ['ICN'] + list(set(sum(tickets,[]))-{'ICN'})
    g = {x:[] for x in t}
    g['S'] = ['ICN']
    for x in tickets:
        g[x[0]].append(x[1])
    
    s = ['ICN']
    tn = 'S'
    v = []
    while s:
        n = s.pop()
        if n in g[tn]:
            g[tn].remove(n)
        else:
            tn = v.pop()
            while n not in g[tn]:
                g[v[-1]].insert(0,tn)
                tn = v.pop()
            g[tn].remove(n)
            v.append(tn)
        v.append(n)
        s += sorted(g[n],reverse=True)
        tn = n
    return v

    # s = 'ICN'
    # v = [tickets.pop(0)]
    # i = 0
    # while tickets:
    #     x = v.pop()
    #     if tickets[i][0] == x[0]:
    #         if tickets[i][1] < x[1]:
    #             print(tickets[i],i)
    #             v.append(tickets.pop(i))
    #             tickets.append(x)
    #             i = 0
    #             continue
    #     i += 1
    #     v.append(x)
    #     print(v,tickets,i)
        


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))
# print(solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]))
# print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
# print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]))
print(solution([['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']]))