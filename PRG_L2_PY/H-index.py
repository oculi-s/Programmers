def solution(citations):
    citations.sort(reverse=True)
    for i,x in enumerate(citations):
        if i+1 > x:
            return i
    return i+1