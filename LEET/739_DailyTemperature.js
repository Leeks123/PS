/**
 * @param {number[]} T
 * @return {number[]}
 */
 var dailyTemperatures = function(T) {
    let max = Math.max(...T);
    let answer = [];
    
    const getBiggerThan = (n,arr) => {
        for(let i=0;i<arr.length;i++) {
            if(arr[i] > n) return i+1;
        }
        return 0;
    }
    
    for(let i=0;i<T.length;i++){
        if(T[i] === max) answer.push(0);
        else {
            answer.push(getBiggerThan(T[i],T.slice(i+1)));
        }
    }
    return answer;
};