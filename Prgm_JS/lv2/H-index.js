function solution(citations) {
    let answer = 0;
    for(let i=1;i<=Math.max(...citations);i++){
        const overH = citations.filter(v => v>=i);
        if(overH.length >= i) {
            answer = answer > i ? answer:i;
        }
    }
    return answer;
}