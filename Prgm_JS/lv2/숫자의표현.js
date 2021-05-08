function solution(n) {
    let arr = [];
    for(let i=1;i<=parseInt(n/2)+1;i++){
        arr.push(i);
    }
    
    const getSumInRange = (start,end,array) => {
        let sum = 0;
        if (start < 0 || start >= array.length || end < 0 || end >= array.length) {
            return 0;
        }
        for(let i= start; i<=end;i++) {
            sum+=array[i];
        }
        return sum;
    }
    
    let start = 0;
    let end = 1;
    let answer = 0;
    while(start < arr.length-1) {
        // console.log(start,end,getSumInRange(start,end,arr));
        if(getSumInRange(start,end,arr) < n) {
            end++;
        } else if(getSumInRange(start,end,arr) == n) {
            answer++;
            start++;
            end = start+1;
        } else {
            start++;
            end = start+1;
        }
    }
    
    return answer+1;
}