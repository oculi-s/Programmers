# def solution(s):
#     a = []
#     for x in s:
#         i = x.index('110')
#         x = x[:i] + x[i+3:]
#         if x in ['1','11']:
#             x = '110' + x
#         elif '111' in x:
#             i = x.index('111')
#             x = x[:i] + '110' + x[i+3:] + '111'
#         else:
#             x += '110'
#         a.append(x)
#     return a

# def solution(s):
#     a = []
#     for x in s:
#         i = 0
#         while i < len(x)-2 and '110' in x:
#             if x[i:i+3] == '110':
#                 x = x[:i] + x[i+3:]
#                 if '111' in x:
#                     x = x.replace('111','110111')
#                 elif x in ['1','11']:
#                     x = '110' + x
#                 else:
#                     x = x + '110'
#             i += 1
#         a.append(x)
#     return a

def solution(s):
    a = []
    for x in s:
        b = 0
        while '110' in x:
            b += x.count('110')
            x = x.replace('110','')
        if '111' in x:
            i = 0
            while i < len(x)-2:
                if x[i:i+3] == '111':
                    x = x[:i] + '110111' + x[i+3:]
                    i += 3
                    b -= 1
                i += 1
            a.append(x+'110'*b)
        else:
            if x in ['1','11']:
                a.append('110'*b+x)
            else:
                a.append(x+'110'*b)
    return a

def solution(s):
    s = ' '.join(s)
    n = 0
    while '1'*n+'1110' in s:
        n += 1
    while n:
        s = s.replace('1'*n+'110','110'+n*'1')
        n -= 1
    return s.split()

print(solution(["1110","100111100","0111111010"]))
print(solution(["1110",'11110']))
print(solution(["0110",'11110']))
print(solution(['111111111111111111000000000000000']))
print(solution(["1011110","01110","101101111010"]))
#11110
#11101
#11011

#100111100
#100111010
#100110110

#0111111010
#0111110110
#0111101110
#0110101101