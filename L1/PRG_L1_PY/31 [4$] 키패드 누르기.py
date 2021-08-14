def solution(numbers, hand):
    answer = ''
    hand = (hand == 'right')*'R'+(hand == 'left')*'L'
    (l,r) = (10,12)

    for n in numbers:
        n = n or 11
        if n in [1, 4, 7]:
            answer += 'L'
        elif n in [3, 6, 9]:
            answer += 'R'
        else:
            dl = abs(n-(l+1))/3+1
            dr = abs(n-(r-1))/3+1
            if l in [2, 5, 8, 11]:
                dl = abs(n-l)/3
            if r in [2, 5, 8, 11]:
                dr = abs(n-r)/3

            if dl > dr:
                answer += 'R'
            elif dl < dr:
                answer += 'L'
            else:
                answer += hand

        if answer[-1] == 'R':
            r = n
        else:
            l = n
    return answer


print(solution([0,0,0,0,0], 'right'))
