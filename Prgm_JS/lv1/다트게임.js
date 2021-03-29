function solution(dartResult) {
    let answer = 0;
    let prevValue = 0

    while (dartResult.length!=0) {
        console.log(dartResult);
        let num = parseInt(dartResult);
        dartResult = dartResult.slice((num+'').length,);
        let bonus = dartResult[0];
        dartResult = dartResult.slice(1,);
        let value = Math.pow(num,bonus === 'S' ? 1 : bonus === 'D' ? 2 : 3);
        
        if(isNaN(parseInt(dartResult)) && dartResult!=='') { // 옵션이 있음
            let option = dartResult[0];
            dartResult = dartResult.slice(1,);
            if(option==='*') {
                answer = answer+ prevValue+2*value
                prevValue = 2*value;
            } else {
                prevValue = value*(-1)
                answer+=prevValue
            }
        } else { // 옵션이 없음
            answer+= value;
            prevValue = value;
        }
        
        console.log(prevValue,answer);
    }
    return answer;
}