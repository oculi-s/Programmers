def solution(n, arr1, arr2):
    answer = ['']*n
    for i in range(n):
        answer[i] += bin(arr1[i] | arr2[i]).replace('0b','').rjust(n).replace('1','#').replace('0',' ')
    return answer

print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))