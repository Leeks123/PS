function countBinaryOne(n) {
    let bin = n.toString(2);
    let count = 0;
    for(let i=0;i<bin.length;i++){
        if(bin[i]=='1') count++;
    }
    return count;
}
function solution(n) {
    let srcOneCount = countBinaryOne(n++);
    while(true) {
        if(srcOneCount == countBinaryOne(n)) {
            break;
        }
        n++;
    }
    return n;
}
