function solution(progresses, speeds) {
    var answer = [];
    
    const restDays = progresses.map((p,i) => {
        return Math.ceil((100-p)/speeds[i])
    });
    
    let cur = restDays[0];
    let deployCount = 1;
    for(let i=1;i<restDays.length;i++){
        if(restDays[i] <= cur) {
            deployCount++;                
        } else {
            answer.push(deployCount);
            cur = restDays[i];
            deployCount = 1;
        }
    }
    answer.push(deployCount);
    
    return answer;
}