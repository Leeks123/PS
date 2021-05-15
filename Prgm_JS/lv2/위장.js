function solution(clothes) {
    const closet = {};
    clothes.forEach(v => {
        if(closet[v[1]]) {
            closet[v[1]].push(v[0]);
        } else {
            closet[v[1]] = [v[0]];
        }
    });
    
    let answer = 1;
    Object.keys(closet).forEach((type) => {
        answer *= closet[type].length+1;
    });
    
    return answer-1;
}