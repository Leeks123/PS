/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
    let allProduct = 1;
    let exceptZeroProduct = 1;
    let zeroCounter = 0;
    for(let v of nums){
        allProduct*=v;
        if(v !== 0) {
            exceptZeroProduct*=v;
            
        } else {
            zeroCounter++;
        }
    }
    
    return nums.map((v) => {
        if(v==0) {
            if(zeroCounter == 1) {
                return exceptZeroProduct;    
            }
            return 0;        
        }
        return parseInt(allProduct/v);
    })
};