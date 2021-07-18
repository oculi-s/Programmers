def solution(n, build_frame):
    M = [[[0]*(n+1) for _ in range(n+1)] for _ in range(2)]
    for x, y, a, b in build_frame:
        if b:
            if 0 in (x,y) or M[a][y][x] or M[1-a][y][x] or a * M[1-a][y][x+1]:
                M[a][y][x] += 1
                M[a][y+(1-a)][x+a] += 1
        else:
            go = False
            M[a][y][x] -= 1
            M[a][y+(1-a)][x+a] -= 1

            # 기둥을 뺄 때 밑에 기둥이 있었거나 : M[0][y][x]
            # 보를 뺄 때 양 옆에 보가 있었거나 : M[1][y][x-1], [x+1]
            if M[a][y][x-a] or M[a][y][x+a]:
                go = True
            if go:
                M[a][y][x] += 1
                M[a][y+(1-a)][x+a] += 1


            # for n in range(n+1):
            #     for m in range(n+1):
            #         if M[1][n][m] == 1:
            #             if not M[0][n][m]:
    R = []
    for x in range(n+1):
        for y in range(n+1):
            for a in [0,1]:
                if M[a][y][x]:
                    R.append([x,y,a])
                    M[a][y][x] -= 1
                    M[a][y+(1-a)][x+a] -= 1
    return R

    for x in reversed(M[0]):
        print(x)
    print("\n")
    for x in reversed(M[1]):
        print(x)
    # return M
    

# 기둥의 시작점 = 1
# 기둥의 시작 + 보의 끝 = 2
# 보의 시작 + 보의 끝 = 3
# 기둥의 끝 + 보의 시작 = 4
# 기둥의 끝점 = 2
# 기둥의 시작 + 보의 시작 = 3
# 기둥의 끝 + 보의 끝 = 5

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1], [5,1,0,0]]))
# print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))