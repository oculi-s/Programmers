import timeit

### 1
# temp = filter(lambda x:not sum([not x%e for e in answer]),range(3,n+1))
# print(list(temp))
# [answer.append(x) for x in range(3,n+1) ]
# for x in range(3,n+1):
# 	if x % t
# 	print(go)
# 	:
# 		answer.append(x)

### 2
# def solution(n):
# 	answer = [2]
# 	for x in range(3,n+1):
# 		if not sum([not x%e for e in answer]):
# 			answer.append(x)
# 	return len(answer)

# a = [x for x in a if x%t]


### 3
# def solution(n):
# 	answer = 0
# 	a = set(range(2, n+1))
# 	while a:
# 		t = a.pop()
# 		a -= set(range(t, n+1, t))
# 		answer += 1
# 	return answer

### 4
# def solution(n):
# 	answer = 0
# 	a = dict.fromkeys(range(n,1,-1))
# 	while a:
# 		t = a.popitem()[0]
# 		for x in range(2*t,n+1,t):
# 			if x in a.keys():
# 				del a[x]
# 		answer += 1
# 	return answer

t1 = timeit.timeit(lambda: print(solution(10000)), number=1)
print(round(t1, 4))