function solution(arr) {
	var answer = [arr[0]];
	for (var i=1; i<arr.length; i++) {
		var e = arr[i];
		if (answer[answer.length-1] != e) {
			answer.push(e)
		}
	}
	return answer
}

console.log(solution([1,1,3,3,0,0,1]))