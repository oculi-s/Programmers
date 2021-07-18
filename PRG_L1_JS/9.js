function solution(n){
	var box = []
	while (parseInt(n/3)){
		box.push(n%3);
		n = parseInt(n/3)
	}
	box.push(n)

	var a = 0;
	for (var i in box){
		var s = box[box.length-i-1] * Math.pow(3,i)
		a += s;
	}
	return a
}
console.log(solution(125))