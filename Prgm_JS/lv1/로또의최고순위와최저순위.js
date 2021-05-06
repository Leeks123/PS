function solution(lottos, win_nums) {
    let matchCount = 0;
    let zeroCount = 0;
    
    lottos.forEach((n) => {
        if(n==0) {
            zeroCount++;
            return;
        }
        if(win_nums.includes(n)) {
            matchCount++;
            win_nums.splice(win_nums.indexOf(n),1);
        }
    });
    console.log(matchCount, zeroCount)
    
    return [matchCount+zeroCount > 1 ? 7-matchCount-zeroCount: 6,
            matchCount > 1 ? 7-matchCount: 6]
}