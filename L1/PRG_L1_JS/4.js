function solution(answers){
    var score = [0,0,0];
    var a = ['12345','21232425','3311224455'];
    for (var i=0; i<answers.length; i++){
        for (var j=0; j<3; j++){
            var pattern = a[j]
            var i2 = i%pattern.length;
            if (answers[i] == parseInt(pattern[i2])){
                score[j]++;
            }
        }
    }
    var m = Math.max.apply(null,score)
    var answer = [];
    for (var i=0; i<score.length; i++){
        if (score[i] == m){
            answer.push(i+1)
        }
    }
    return answer
}

console.log(solution([1,3,2,4,2]))