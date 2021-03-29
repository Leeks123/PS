function solution(numbers, hand) {
    let answer = '';
    let leftPos = '*';
    let rightPos = '#';
    
    let leftCan = [1,4,7];
    let rightCan = [3,6,9];
    let bothCan = [2,5,8,0];
    
    const calcDistance = (pos,number) => {
        const value = {
            0: [3,2,1,0],
            1: [1,2,3,4],
            2: [0,1,2,3],
            3: [1,2,3,4],
            4: [2,1,2,3],
            5: [1,0,1,2],
            6: [2,1,2,3],
            7: [3,2,1,2],
            8: [2,1,0,1],
            9: [3,2,1,2],
            '#': [4,3,2,1],
            '*': [4,3,2,1]
        };
        return value[pos][bothCan.indexOf(number)];
    }
    
    numbers.forEach(number => {
       if(leftCan.includes(number)) {
           answer+='L';
           leftPos = number;
       } else if(rightCan.includes(number)) {
           answer+='R';
           rightPos = number;
       } else {
           if (calcDistance(leftPos,number) < calcDistance(rightPos,number)) {
               answer+='L';
               leftPos = number;
           } else if(calcDistance(leftPos,number) > calcDistance(rightPos,number)) {
               answer+='R';
               rightPos = number;
           } else {
               if(hand === 'right') {
                   rightPos = number;
                   answer+='R';
               } else {
                   leftPos = number;
                   answer+='L';
               }
           }
       }
        // console.log(leftPos,rightPos,number,answer);
    });
    
    return answer;
}