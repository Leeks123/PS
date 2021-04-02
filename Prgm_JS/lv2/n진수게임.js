function getFullList(n,t,m) {
    let i = 0;
    let answer = '';
    while(answer.length <= m*t) {
        answer += i.toString(n).toUpperCase();
        i++;
    }
    return answer;
}

function solution(n, t, m, p) {
    var answer = '';
    const fullList = getFullList(n,t,m);
    let i = 0;
    // console.log(fullList);
    while(answer.length < t) {
       answer += fullList[p-1 + m*i];
        // console.log(answer);
        i++;
    }
    return answer;
}