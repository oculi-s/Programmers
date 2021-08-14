def solution(m, n, board):
    b = [list(x) for x in zip(*board)]
    d = set()
    a = 0
    while True:
        for x in range(n-1):
            for y in range(m-1):
                t = [b[x][y], b[x+1][y], b[x][y+1], b[x+1][y+1]]
                if sum(z == t[0] for z in t if z != ' ') == 4:
                    d.add((x, y))
        a += len(d) * 4
        for p in d:
            x, y = p
            t = [b[x][y], b[x+1][y], b[x][y+1], b[x+1][y+1]]
            b[x][y], b[x+1][y], b[x][y+1], b[x+1][y+1] = '', '', '', ''
            a -= t.count('')
        b = [list(''.join(x).rjust(m)) for x in b]
        if not d:
            return a
        d = set()

print(solution(	4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
