const binaryConvert = (s) => {
    let len = s.length;
    let p = new RegExp('0','g');
    s = s.replace(p,'');
    return { 
        retStr: (s.length).toString(2), 
        deleted: len-s.length }
}
function solution(s) {
    let answer = [0,0];
    
    while(s != '1') {
        let { retStr, deleted } = binaryConvert(s);
        s = retStr;
        answer[0] += 1;
        answer[1] += deleted;
    }
    
    return answer;
}