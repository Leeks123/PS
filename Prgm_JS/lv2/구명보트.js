function solution(people, limit) {
    let count = 0;
    people.sort((a,b)=>b-a);
    while(people.length) {
        let p = people.shift();
        let ret = people.findIndex(v => v <= limit-p);
        
        if(ret !== -1) {
            people.splice(ret,1);
        }
        count++;
    }
    return count;
}