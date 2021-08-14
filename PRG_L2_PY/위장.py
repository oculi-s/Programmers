def solution(clothes):
    d = dict()
    for x in clothes:
        if not x[1] in d:
            d[x[1]] = 1
        else:
            d[x[1]] += 1
    t = 1
    for x in d.values():
        t *= x + 1
    return t - 1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
