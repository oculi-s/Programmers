def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    F = sorted([[v, i+1] for i, v in enumerate(food_times)])
    S, N = 0, len(F)
    for i, v in enumerate(F):
        k -= (N-i)*(v[0]-S)
        if k <= 0:
            k += (N-i)*(v[0]-S)
            t = sorted(F[i:], key=lambda c: c[1])
            return t[k % (N-i)][1]
        S += (v[0]-S)

print(solution([3, 1, 2], 5), 1)
print(solution([15, 5, 2], 20), 1)
print(solution([6, 15, 2], 20), 2)
print(solution([7, 7, 7], 20), 3)
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16), 3)
print(solution([4, 2, 3, 6, 7, 1, 5, 8], 27), 5)
8765
