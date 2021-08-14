def solution(cacheSize, cities):
    c = []
    v = 0
    while cities:
        x = cities.pop(0).lower()
        if x not in c:
            v += 5
            c.append(x)
            if len(c) > cacheSize:
                c.pop(0)
        else:
            c.remove(x)
            c.append(x)
            v += 1
    return v

print(solution(0,list('23141')))
# print(solution(0,["Jeju",'jeju','jeju']))
# print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))