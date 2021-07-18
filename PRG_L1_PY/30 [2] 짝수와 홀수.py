def solution(num):
    x = num%2
    answer = "Odd"*x + "Even"*(not x)
    return answer
