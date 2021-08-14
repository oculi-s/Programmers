def solution(arr, divisor):
	# [1,2,3,4] x>3 --> 3 x<=3 --> -3
	# [-1,-1,-1,1]

	# for i in range(len(arr)):
	# 	arr[i] = 3*(arr[i]>3 or -1)

    answer = [e for e in arr if not e%divisor] or [-1]
    return sorted(answer)

def solution(arr,divisor):
	box = []
	for i in arr:
		if not i % divisor:
			box.append(i)
# 	if not box:
# 		# box가 비어있을 때
# 		# if문을 하나도 통과하지 않아서 append가 되지 않았을 때
# 		box.append(-1)
	# or : if box == None:
	# 			 box or a = a
	return sorted(box or [-1])