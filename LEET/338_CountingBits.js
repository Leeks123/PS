/**
 * @param {number} num
 * @return {number[]}
 */
 var countBits = function(num) {
    const counter = (n) => {
        let s = n.toString(2);
        let ret = 0;
        for(let i=0;i<s.length;i++){
            if(s[i]==1){
                ret++;
            }
        }
        return ret;
    }
    
    let ret = [];
    for(let i=0;i<=num;i++){
        ret.push(counter(i));
    }
    return ret;
};