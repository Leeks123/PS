function solution(msg) {
    var answer = [];
    let dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');

    while (msg.length > 0) {
        for(let i=0;i<msg.length;i++){
            const slicedMsg = msg.slice(0,msg.length-i);
            if(dict.includes(slicedMsg)) {
                answer.push(dict.indexOf(slicedMsg)+1)
                dict.push(msg.slice(0,msg.length-i+1));
                msg = msg.slice(slicedMsg.length,);
                break;
            }
        }
    }
    return answer;
}