def solution(brown, yellow):
    b = brown//2
    for x in range(2,b):
        if (x+1)*(b-x+1) == brown+yellow:
            return [b-x+1,x+1]

print(solution(10,2))