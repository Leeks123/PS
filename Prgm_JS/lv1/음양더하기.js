function solution(absolutes, signs) {
    return absolutes.reduce((acc,v,i) => {
        if(signs[i]) {
            return acc + v;
        } else {
            return acc + v*(-1);
        }
    },0)
}