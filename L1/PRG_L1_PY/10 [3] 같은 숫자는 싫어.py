### 1
# def solution(arr):
# 	i = arr.pop(0)
# 	# pop은 del을 안써도 됨.
# 	answer = [i]
# 	while arr:
# 		# 하나씩 뽑으면서 하나라도 남아있을 때까지만
# 		if arr[0] != i:
# 			answer.append(arr[0])
# 		i = arr.pop(0)
# 		# 뽑음과 동시에 지워준다.
# 	return answer
# print(solution([1,1,3,3,0,1,1]))

###2
# def solution(arr):
# 	answer = [arr.pop()]
# 	for _ in range(len(arr)):
# 		# answer = [arr.pop(), answer[1:] if answer[-1] != arr.pop()]
# 		x = arr.pop()
# 		# print(arr,answer)
# 		if answer[0] != x:
# 			answer.insert(0,x)
# 			# answer.append(arr.pop(0))
# 	return answer

###3
# def solution(arr):
# 	answer = arr[:1] # arr[:1] = [1] /// arr[0] = 1
# 	for e in arr[1:]: 
# 		# 두개로 나눔 맨 첫놈 / 들어올 놈
# 		if answer[-1] != e:
# 			# 만약 가장 최근에 들어온 놈이 지금 들어올놈과 다르면
# 			answer.append(e)
# 			# answer에 추가해준다
# 	return answer

# arr = [1,1,3,3,0,1,4]
# print(solution(arr))
