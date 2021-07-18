def solution(answers):
    score = [0,0,0]
    a = ['12345','21232425','3311224455']
    
    for i in range(len(answers)):
        for j in range(3):
            i2 = i%len(a[j])
            pattern = a[j]
            if answers[i] == int(pattern[i2]):
                score[j] = score[j] + 1
    score = [i+1 for i,j in enumerate([x == max(score) for x in score]) if j]
    return score

print(solution([1,3,2,4,2]))