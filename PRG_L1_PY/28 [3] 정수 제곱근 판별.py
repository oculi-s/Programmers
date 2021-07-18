def solution(n):
	answer = int((n**.5).is_integer()*((n**.5+1)**2+1)-1)
	return answer

print(solution(3))