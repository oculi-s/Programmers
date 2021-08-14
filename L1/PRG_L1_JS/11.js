function solution(arr, divisor) {
	var answer = [];
	for (var i=0; i<arr.length; i++){
		if (!arr[i]%divisor)
			answer.push(arr[i])
	}
    return answer.sort();
}