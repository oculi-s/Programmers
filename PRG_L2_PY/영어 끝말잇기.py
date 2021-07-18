def solution(n, words):
    a = [0,0]
    while len(words) > 1:
        x = words.pop()
        if x in words or x[0] != words[-1][-1]:
            a = [len(words)%n+1,len(words)//n+1]
    return a