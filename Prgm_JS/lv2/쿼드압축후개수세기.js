// 하나 시간 초과
function isAllSame(arr) {
    const init = arr[0][0];
    for(let i=0;i<arr.length;i++){
        for(let j=0;j<arr.length;j++){
            if(arr[i][j] !== init){
                return false;
            }
        }
    }
    return init;
}
function splitArr(arr) {
    let ret = [[],[],[],[]];
    for(let i=0; i<arr.length/2; i++) {
        let temp = [[],[],[],[]]
        for(let j=0; j<arr.length/2; j++) {
            temp[0].push(arr[i][j]);
            temp[1].push(arr[arr.length/2+i][j]);
            temp[2].push(arr[i][arr.length/2+j]);
            temp[3].push(arr[arr.length/2+i][arr.length/2+j]);
        }
        for(let j=0;j<4;j++){
            ret[j].push(temp[j]);
        }
    }
    return ret;
}
function solution(arr) {
    let answer = [0,0];
    let q = [arr];
    
    while(q.length>0) {
        let checkingArr = q.shift();
        let ret = isAllSame(checkingArr);
        // console.log(checkingArr,ret);
        if(ret === false){
            q = [...q,...splitArr(checkingArr)];
        } else {
            answer[ret]++;
        }
    }
    
    return answer;
}