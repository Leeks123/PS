function getMultiSet(str){
    let ret = [];
    const re = /[a-z]+/;
    
    let duplicate = [];
    for(let i=0;i<=str.length-2;i++){
        const token = str.slice(i,i+2);
        const check = re.exec(token)
        if (check === null) continue;
        else if(token === re.exec(token)[0]) {
            if(ret.includes(token)) {
                duplicate.push(token);
            } else {
                ret.push(token); 
            }
        }
    }
    duplicate = duplicate.sort();
    let counter = 1;
    console.log(ret,duplicate)
    for(let i=0;i<duplicate.length-1;i++){
        ret.push(duplicate[i]+counter);
        if(duplicate[i+1]!==duplicate[i]) {
            counter = 1;
        } else {
            counter++;
        }
        if(i===duplicate.length-2) {
            ret.push(duplicate[duplicate.length-1]+counter);
        }
    }
    if(duplicate.length === 1) {
        ret.push(duplicate[0]+counter)
    }
    console.log(ret);
    return ret;
}
function intersect(arr1,arr2) {
    let ret = [];
    const lArr = arr1.length > arr2.length ? arr1 : arr2;
    const sArr = arr1.length <= arr2.length ? arr1 : arr2;
    
    sArr.forEach((e) => {
        if (lArr.includes(e)) {
            ret.push(e);
        }
    });
    console.log('inter',ret)
    return ret;
}
function union(arr1,arr2) {
    let ret = [];
    const lArr = arr1.length >= arr2.length ? arr1 : arr2;
    const sArr = arr1.length < arr2.length ? arr1 : arr2;
    
    sArr.forEach((e) => {
        if (!lArr.includes(e)) {
            ret.push(e);
        }
    });
    console.log('union',ret,lArr);
    return [...ret,...lArr];
}

function solution(str1, str2) {
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    
    const multiset1 = getMultiSet(str1);
    const multiset2 = getMultiSet(str2);
    
    let inst = intersect(multiset1,multiset2).length;
    let unio = union(multiset1,multiset2).length;
    let ret =  unio!==0 ? inst/unio : 1
    return Math.floor(ret*65536);
}