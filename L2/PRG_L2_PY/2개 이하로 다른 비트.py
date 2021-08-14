def solution(numbers):
    a = []
    for x in numbers:
        b = bin(x)
        i = 1
        while b[-i] == '1':
            i += 1
        if i == 1:
            a.append(x+1)
        else:
            a.append(x-2**(i-2)+2**(i-1))
    return a

print(solution([2,7]))