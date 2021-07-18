def solution(num):
    c = 0
    while num-1:
        c += 1
        if num % 2:
            num = num*3 + 1
        else:
            num /= 2
        if c == 500:
            return -1
    return c

print(solution(6))
