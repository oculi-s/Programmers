def solution(lottos, win_nums):
    m = min(7 - len(set(lottos) & set(win_nums)),6)
    return m-lottos.count(0) or 1, m


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
