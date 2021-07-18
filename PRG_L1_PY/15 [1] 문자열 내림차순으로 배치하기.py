def solution(s):
	l = [x for x in s if x.islower()]
	u = [x for x in s if x.isupper()]
	answer = ''.join(reversed(sorted(u)+sorted(l)))
	return answer

print(solution("Zbcdefg"))