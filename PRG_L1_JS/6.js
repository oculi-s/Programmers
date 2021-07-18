function solution(a, b){
    var d = [31,29,31,30,31,30,31,31,30,31,30,31];
    for (var i=0; i<a-1; i++){
        b += d[i]
	}
    var answer = ["FRI","SAT","SUN","MON","TUE","WED","THU"][(b-1)%7]
    return answer;

}

console.log(solution(1,8))