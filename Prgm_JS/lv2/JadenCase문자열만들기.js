function solution(s) {
    s = s.toLowerCase();
    s = s[0].toUpperCase().concat(s.slice(1));
    
    for(let i=1;i<s.length;i++){
        if(s[i] !== ' ') {
            if(s[i-1] == ' '){
                s = s.slice(0,i)+s[i].toUpperCase()+s.slice(i+1)
            }
        }
    }
    return s
}