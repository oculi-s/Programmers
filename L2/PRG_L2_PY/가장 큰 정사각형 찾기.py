def solution(board):
    m = len(board[0])
    n = len(board)
    b = [list(x) for x in zip(*board)]
    a = int(any([1 in a for a in board]))
    y = -1
    while n-y-1 > a:
        x = -1
        y += 1
        while m-x-1 > a:
            x += 1
            if board[y][x]:
                l = 1
                while l < m-x and l < n-y:
                    if 0 in b[x+l][y:y+l+1]:
                        x += l
                        break
                    elif 0 in board[y+l][x:x+l]:
                        x += l - 1 - list(reversed(board[y+l][x:x+l])).index(0)
                        break
                    l += 1
                if l > a:
                    a = l
    return a ** 2

print(solution(	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[0, 0, 0, 0], [0, 0, 0, 0]]))
print(solution([[0, 1, 1, 1], [1, 1, 1, 0]]))
print(solution([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]))
print(solution(	[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 1, 1, 1]]))