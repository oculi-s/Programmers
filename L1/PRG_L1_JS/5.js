function solution(array, commands) {
    var answer = [];
    for (var i in commands){
        var c = commands[i];
        answer.push(array.slice(c[0]-1,c[1]).sort((a,b)=>a-b)[c[2]-1])
    }
    return answer;
}