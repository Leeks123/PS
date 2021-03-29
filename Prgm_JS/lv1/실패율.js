function solution(N, stages) {
    let counter = Array(N+1).fill(0);
    stages.forEach((v) => {
        counter[v-1]++;
    });
    let failRates = []
    const sum = stages.length;
    let accum = 0
    counter.forEach((v,i) => {
        failRates.push(v/(sum-accum));
        accum+=v
    })
    let answer = failRates.
        slice(0,failRates.length-1).
        map((v,i) => {
            let ret = [v,i+1];
            return ret;
        }).
        sort((a,b) => b[0]-a[0]).
        map((v) => v[1]);
    return answer;
}