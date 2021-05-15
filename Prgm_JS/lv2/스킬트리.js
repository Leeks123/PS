function isAble(skill_list,skill) {
    let ptr = 0;
    for(let i=0;i<skill_list.length;i++){
        // console.log(skill[ptr],skill_list[i]);
        if(ptr == skill.length) break;
        if(skill[ptr] == skill_list[i]){
            ptr++;
        } else {
            if(skill.slice(ptr+1).includes(skill_list[i])){
                return false;
            }
        }
    }
    return true;
}
function solution(skill, skill_trees) {
    var answer = 0;
    
    skill_trees.forEach((v) => {
        if(isAble(v,skill)){
            answer++;
        }
    });
    
    return answer;
}