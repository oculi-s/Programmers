function solution(participant, completion) {
    participant.sort()
    completion.sort()
    completion.push('zzzzzzz');

    for (var i=0; i<completion.length; i++){
        if (participant[i] != completion[i]){
            return participant[i]
        }
    }
}

var p = ["mislav", "stanko", "mislav", "ana"]
var c = ["stanko", "ana", "mislav"]
console.log(solution(p,c))