function solution(n) {
    let answer = '';

    while(n !== 0) {
        let div = Math.floor(n/3);
        let mod = n%3;
        if(mod == 0) {
            answer = 4+answer;
            n = div-1;
        } else {
            answer = mod+answer;
            n = div;
        }
    }
    
    return answer;
}