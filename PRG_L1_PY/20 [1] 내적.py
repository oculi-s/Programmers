
# def solution(a, b):
#     answer = sum([x*y for x,y in zip(a,b)])
#     return answer

a = ['a','b','c','d'] #이름
b = [-3,-1,0,2] #성적
d = {x:y for x,y in zip(a,b)}
print(d['a']) #dict[이름]

# print([x for x,y in [[1,-3],[2,-1],[3,0],[4,2]]])
# print([i for i in [{1,-3},{2,-1},{3,0},{4,2}]])

