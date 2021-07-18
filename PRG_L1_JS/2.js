function solution(numbers) {
    var answer = [];
    var l = numbers.length;
    for (var i = 0; i < l; i++) {
        for (var j = i + 1; j < l; j++) {
            var number = numbers[i] + numbers[j];
            if (!answer.includes(number)) {
                answer.push(number);
            }
        }
    }
    return answer.sort((a,b)=>a-b);
}
solution([2, 1, 3, 4, 1])