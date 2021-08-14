# def solution(arr):
#     arr[::2] = [int(x) for x in arr[::2]]
#     r = [arr]
#     while len(r[0]) > 1:
#         t = []
#         for x in r:
#             for i in range(0, len(x)-1, 2):
#                 v = x[:i] + \
#                     [x[i]+((x[i+1] == '+')-(x[i+1] == '-'))*x[i+2]]+x[i+3:]
#                 if v not in t:
#                     t.append(v)
#         r = t
#     return max(r)[0]

def solution(arr):
    arr[::2] = [int(x) for x in arr[::2]]
    i, m = 1, 0
    while i < len(arr):
        if arr[i] == '+':
            if i >= 3:
                if '+' not in arr[:i]:
                    i += 2
            if arr[i] == '+':
                arr[i-1] = arr.pop(i+1) + arr.pop(i-1)
                i -= 2
        i += 2
    r = arr[::2]
    if len(r) < 2:
        return r[0]
    else:
        if '+' in arr:
            m = arr[arr.index('+') + 1]
        return r[0]-r[1]+abs(sum(r[2:])-2*m)

def solution(arr):
    arr[::2] = [int(x) for x in arr[::2]]
    I = []
    for i in range(1, len(arr), 2):
        if arr[i] == '-':
            I.append(i+1)
    v = 0
    if not I:
        v += sum(arr[::2])
    else:
        v += sum(arr[:I[0]:2])-arr[I[0]]
        v += sum(arr[I[-1]+2::2])
    for i in reversed(range(len(I)-1)):
        print(v)
        s = sum(arr[I[i]+2:I[i+1]:2])
        v += abs(s - arr[I[i+1]])
    return v
# + - + -
# 1 3 5 8

# 절댓값이 최소인 양수
# 절댓값이 최소인 음수

def solution(arr):
    T = [0,0]
    s = 0
    for n in reversed(range(len(arr))):
        if arr[n][0] in '1234567890':
            s += int(arr[n])
        elif arr[n][0] == '-':
            print(T,s)
            a = min(-(T[1]+s),T[0]-s)
            b = max(-(T[0]+s),T[1]+s-2*int(arr[n+1]))
            T = [a, b]
            s = 0
            print(T)
    return T[1] + s

def solution(arr):
    a, b, s = 0, 0, 0
    for i in reversed(range(-1,len(arr),2)):
        s += int(arr[i+1])
        if arr[i] == '-':
            ta = [a-s,-b-s]
            tb = [-a-s,b+s-2*int(arr[i+1])]
            a, b = min(ta), max(tb)
            s = 0
    return b + s

# print(solution(["1", "+", "2"]),3)
# print(solution(["1", "+", "2", "-", "2", "-", "2"]),3)
# print(solution(["1", "-", "2"]),-1)
# print(solution(["1", "-", "2", "-", "2", "-", "2", "-", "2", "-", "2", "-", "2"]),9)
# print(solution(["1", "-", "3", "-", "5", "-", "8"]),11)
# print(solution(["1", "-", "3", "+", "5", "-", "8"]),1)
# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]),3)
# print(solution(["5", "+", "3", "+", "1", "+", "2", "-", "4"]),7)
# print(solution(["5", "+", "3", "-", "1", "+", "2", "-", "4"]),9)
print(solution(["9", "-", "1", "-", "1", "-", "1", "-", "31", "-", "1", "+", "10","+", "10","+", "10","-", "1",'+','1','+','1']),73)
# print(solution(["9", "-", "1", "+", "1", "+", "1", "-", "31", "-", "1", "+", "10","+", "10","+", "10","-", "1",'+','1','+','1']),73)