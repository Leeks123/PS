function solution(record) {
    const guestBook = {};
    const result = [];
    record
    .map((cmd) => cmd.split(' '))
    .forEach((cmd) => {
        if(cmd[0] === 'Enter') {
            guestBook[cmd[1]] = cmd[2];
            result.push([cmd[1],`님이 들어왔습니다.`]);
        } else if(cmd[0] === 'Leave') {
            result.push([cmd[1],`님이 나갔습니다.`]);
        } else {
            guestBook[cmd[1]] = cmd[2];
        }
    });
    return result.map((v) => guestBook[v[0]]+v[1]);
}