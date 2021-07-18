def solution(participant, completion):
# define f(x):
#   return 2
# a = f(x) (a=2)

# 1
# a = [leo, kiki, eden]
# b = [eden, kiki]

# c = [leo,kiki,eden,eden,kiki]
# set(c)
# [leo,kiki,eden]

# mylist = ["leo","kiki","eden"]
# mylist[0] = "leo"
# mylist[0][0] = "l"

# 2
# 둘이 다르면!
    # a = []
    # # 인덱스로 돌리기
    # for i in participant:
    #     if not i in completion:
    #         a.append(i)
    # return a[0]
    # (1)
    # if 둘이 다르면:
    #     a.append(결과를 넣는다)
    # (2)
    # if j 가 i 에 없으면:

    completion.append('zzzzzzzzzzzzzzz')
    for x,y in zip(sorted(participant),sorted(completion)):
        if x!=y:
            # return 해버리면 함수가 더이상 실행되지 않는다
            return x

p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
# "leo"
print(solution(p,c))
