function solution(str){
	var n = parseInt(str.length/2);
	var answer = str[n-1] + str.length%2 ? '':str[n];
	return answer;
}

console.log(solution("abcdef"))