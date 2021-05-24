function getGCD(a,b) { // a > b;
    if(b===0) return a;
    else {
        return getGCD(b,a%b);
    }
}
function getLCM(a,b) {
    return a*b/getGCD(a,b);
}

function solution(arr) {
    arr = arr.sort((a,b) => b-a);
    let answer = arr[0];
    for(let i=1;i<arr.length;i++){
        answer = getLCM(answer,arr[i]);
    }
    return answer;
}