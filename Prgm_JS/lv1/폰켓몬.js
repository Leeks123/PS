
function solution(nums) {
    let counter = {};
    nums.forEach((v) => {
        if(v in counter) {
            counter[v]++;
        } else {
            counter[v] = 1;
        }
    })
    return Object.keys(counter).length > parseInt(nums.length/2)? parseInt(nums.length/2) : Object.keys(counter).length;
}


// function solution(nums) {
//   const max = nums.length / 2;
//   const arr = [...new Set(nums)];

//   return arr.length > max ? max : arr.length
// }