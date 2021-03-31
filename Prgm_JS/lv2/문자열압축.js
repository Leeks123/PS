function compress(s,n) {
    let tokens = [];
    for(let i=0;i<s.length;i+=n){
        tokens.push(s.slice(i,i+n))
    }
    let counter = 1;
    let answer = '';
    for(let i=1;i<tokens.length;i++){
        if(tokens[i] !== tokens[i-1]){
            answer += counter === 1 ? tokens[i-1] : counter+tokens[i-1];
            counter = 1;
            if(i === tokens.length-1) {
                answer+=tokens[i];
            }
        } else {
            counter++;
            if(i === tokens.length-1) {
                answer += counter+tokens[i-1];
            }
        }
    }
    return answer.length;
}
function solution(s) {
    if(s.length === 1){
        return 1;
    }
    let results = [];
    let i = 1;
    while(i<s.length){
        let result = compress(s,i);
        i++;
        results.push(result);
    }
    console.log(results)
    return Math.min(...results);
}