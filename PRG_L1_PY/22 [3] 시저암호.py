def solution(s, n):
    t = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''.join([t[(t.index(x)+n)%len(t)] if x.islower() else t[(t.index(x.lower())+n)%len(t)].upper() if x.isupper() else x for x in s])
    return answer

print(solution('A B',1))