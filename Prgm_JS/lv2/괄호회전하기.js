const isValid = (s) => {
    let openParen = ['(','[','{'];
    let closeParen = [')',']','}'];
    let stack = [];

    for(let i=0;i<s.length;i++){
        if(openParen.includes(s[i])) {
            stack.push(s[i]);
        } else {
            let poped = stack.pop();
            if(!poped) return false;
            if(closeParen.indexOf(s[i]) !== openParen.indexOf(poped)){
                return false;
            }
        }
        // console.log(stack);
    }
    if(stack.length !== 0) return false;
    return true;
}
const rotate = (s) => {
    return s.slice(1)+s[0];
}
function solution(s) {
    let count = 0;
    let str = s;
    for(let i=0;i<str.length;i++){
        if(isValid(str)){
            count++;
            // console.log(str)
        }
        str = rotate(str);
    }
    
    return count;
}