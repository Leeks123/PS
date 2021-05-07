function solution(numbers) {
    var answer = [];
    
    for(let i=0,len = numbers.length-1;i<len;i++){
        for(let j=i+1,len = numbers.length;j<len;j++){
            if(!answer.includes(numbers[i]+numbers[j])){
                answer.push(numbers[i]+numbers[j]);
            }
        }
    }
    answer.sort((a,b)=>a-b)
    return answer;
}