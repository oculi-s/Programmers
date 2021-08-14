# def solution(s):
# 	# 왼쪽이 짝수, 오른쪽이 홀수
# 	answer =  s[int(len(s)/2)-1] + s[int(len(s)/2)]
# 	# 홀수일 때 통과하겠다.
# 	# 2로 나눈 나머지가 1일 때 통과하겠다
# 	if (len(s)%2):
# 		answer = answer[1]
# 	return answer

# 나보다 잘한사람 풀이 있음

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
print(string_middle("abcdef"))