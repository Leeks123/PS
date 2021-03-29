function solution(n, arr1, arr2) {
    var answer = [];
    const fillZero = (s,n) => {
        // console.log(s,n)
        if(s.length < n) {
            return '0'.repeat(n-s.length)+s;
        }
        return s;
    }
    for(let i=0;i<n;i++){
        let a = arr1[i].toString(2)
        let b = arr2[i].toString(2)
        a = fillZero(a,n);
        b = fillZero(b,n);
        let ret = ''
        for(let j=0;j<n;j++){
            if(a[j]==='0' && b[j]==='0') {
                ret+=' ';
            } else {
                ret+='#';
            }
        }
        answer.push(ret);
    }
    
    return answer;
}