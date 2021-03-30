const preprocess = (s) => {
    s = s.slice(2,s.length-2);
    
    s = s.split('},{');
    s = s.map((v) => v.split(','));
    return s;
}

const filterArr = (arr) => {
    let first = arr[0][0];
    arr = arr.slice(1,);
    if(arr.length===0){
        return [parseInt(first)];
    }else{
        arr.map((a) => {
            const idx = a.indexOf(first);
            a.splice(idx, 1);
        });
        let recur = filterArr(arr);
        return [parseInt(first), ...recur];
    }
}

function solution(s) {
    var answer = [];
    
    let arr = preprocess(s);
    arr = arr.sort((a,b) => a.length - b.length);
    
    answer = filterArr(arr);
    
    return answer;
}