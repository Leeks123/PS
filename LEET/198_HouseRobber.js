/**
 * @param {number[]} nums
 * @return {number}
 */
 var rob = function(nums) {
    let dp = [nums[0]];
    for(let i=1;i<nums.length;i++){
        if(i==1) {
            dp[i] = Math.max(dp[0],nums[i]);        
        } else {
            dp[i] = Math.max(dp[i-2]+nums[i],dp[i-1]);
        }
    }
    return dp[nums.length-1];
};