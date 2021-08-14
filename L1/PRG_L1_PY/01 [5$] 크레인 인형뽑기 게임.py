def solution(board, moves):
    result = 0
    board = [list(x) for x in list(zip(*board))]
    out = []

    for i in range(len(moves)):
        n = moves[i]-1
        for i in range(len(board[n])):
            if board[n][i] != 0:
                out.append(board[n][i])
                board[n][i] = 0
                break
        print(out)

    while sum([out[j]==out[j+1] for j in range(len(out)-1)]):
        for i in range(len(out)-1):
            if out[i] == out[i+1]:
                del out[i:i+2]
                result = result + 1
                break
    return result * 2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))