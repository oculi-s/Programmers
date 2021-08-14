def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
    return answer


# i가 어디서부터 j가 어디까지
# 정렬을 해주고
# 정렬을 한 상태에서 K번째 수뽑기
# def solution(array, commands):
#     answer = []
#     # range(2,5)
#     # 2,3,4
    
#     # a = [1,2,3,4,5]
#     # a[1:]

#     # i는 요소! sorted(배열)
#     # 배열.sort() 하면 새로운 변수에 넣지 않아도 됨
#     # 배열2 = sorted(배열1) 해줘야 sorted된 배열1이 배열2에 들어감.

#     # 배열.index(요소) = 인덱스
#     # 배열[인덱스] = 요소

#     # 2,3,5,6
#     # 2,5,3
#     # commands[2] = 3
#     answer = sorted(array[c[0]-1:c[1]])[c[0][2]-1]
#     return answer

array = [1,5,2,6,3,7,4]
# commands = [2,5,3]
commands = [[2,5,3],[4,4,1],[1,7,3]]
print(solution(array,commands))
# print(list(enumerate(array)))
