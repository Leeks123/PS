function rotate2DArray(arr) {
    let ret = [];
    for(let i=0;i<arr[0].length;i++){
        let row = [];
        for(let j=0;j<arr.length;j++){
            row.push(arr[j][i]);
        }
        ret.push(row);
    }
    return ret;
}
function multipleArray(arr1,arr2) {
    let ret = 0;
    for(let i=0;i<arr1.length;i++){
        ret+=arr1[i]*arr2[i];
    }
    return ret;
}
function solution(arr1, arr2) {
    var answer = [];
    let rotatedArr = rotate2DArray(arr2);
    
    arr1.forEach((v) => {
        let row = [];
        rotatedArr.forEach(r => {
            row.push(multipleArray(v,r));
        });
        answer.push(row);
    });
    
    return answer;
}