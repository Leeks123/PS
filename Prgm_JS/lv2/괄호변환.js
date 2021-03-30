const isBalanced = (p) => {
    let leftParen = 0;
    let rightParen = 0;
    
    let arrStr = p.split('');
    if (arrStr.length === 0){
        return true;
    }
    arrStr.forEach((v) => {
        if(v==='(') {
            leftParen++;
        } else {
            rightParen++;
        }
    });
    if (leftParen === rightParen) {
        return true;
    }
    return false;
}
const isCorrect = (p) => {
    let st = [];
    let ret = true;
    let arrStr = p.split('');
    if (arrStr.length === 0){
        return true;
    }
    arrStr.forEach((v) => {
        if(v==='('){
            st.push(v);
        } else {
            const poped = st.pop();
            if(poped !== '('){
                ret = false;
            }
        }
    });
    if(!ret) {
        return ret;
    }
    if(st.length !== 0) {
        return false;
    }
    return true;
}

const trimAndTurn = (p) => {
    p = p.slice(1,p.length-1);
    p = p.replace(/\(/g,'-');
    p = p.replace(/\)/g,'(');
    p = p.replace(/-/g,')');
    return p;
}

function solution(p) {
    let u = '';
    let v = '';
    if(p===''){ // 1
        return '';
    }
    
    if(p.length===2){
        if(isBalanced(p)){
            u = p;
            v = '';
        }
    } else {
        for(let i=2;i<=p.length;i++){ // 2
        if(isBalanced(p.slice(0,i))){
            u = p.slice(0,i);
            v = p.slice(i,);
            console.log(u,v);
            break;
        }
    }
    }
    
    if(isCorrect(u)) { // 3
        return u + solution(v);
    } else { // 4
        let answer = '('; // 4-1
        answer += solution(v)+')'; // 4-2,3
        answer += trimAndTurn(u);
        return answer;
    }
}