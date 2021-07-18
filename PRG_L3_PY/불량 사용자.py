from itertools import product
def solution(user_id, banned_id):
    g = [set() for _ in range(len(banned_id))]
    for i, x in enumerate(banned_id):
        for y in user_id:
            if len(x) == len(y):
                if not any(a != '*' and a != b for a, b in zip(x,y)):
                    g[i].add(y)
    v = []
    for x in product(*g):
        if len(x) == len(set(x)):
            if not set(x) in v:
                v.append(set(x))
    return len(v)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))