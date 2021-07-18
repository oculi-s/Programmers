def solution(arr1, arr2):
    m,n=(len(arr1),len(arr1[0]))
    answer = [x+y for x,y in zip(sum(arr1,[]),sum(arr2,[]))]
    answer = [answer[n*i:n*(i+1)] for i in range(m)]
    return answer