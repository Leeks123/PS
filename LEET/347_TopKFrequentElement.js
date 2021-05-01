/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var topKFrequent = function(nums, k) {
    let counter = {};
    for(let v of nums) {
        if(v in counter) {
            counter[v]++;
        } else {
            counter[v] = 1;
        }
    }
    let arr = [...Object.keys(counter)];
    arr.sort((a,b) => {
       if(counter[a] >= counter[b]) {
           return -1;
       } else {
           return 1;
       }
    });
    let answer = [];
    for(let i=0;i<k;i++){
        answer.push(+arr[i])
    }
    return answer;
};