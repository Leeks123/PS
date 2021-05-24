function solution(land) {
    let dp = [land[0]];
    
    for(let i=1;i<land.length;i++){
        let row = [];
        for(let j=0;j<4;j++){
            let rest = dp[i-1].filter((v,idx) => idx !== j);
            row.push(land[i][j]+Math.max(...rest));
        }
        // console.log(i,row);
        dp.push(row);
    }
    

    return Math.max(...dp[dp.length-1]);
}