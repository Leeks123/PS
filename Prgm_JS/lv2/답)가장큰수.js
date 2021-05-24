function solution(numbers) {
    let answer = numbers.
        map(number => [number,number.toString().repeat(4).slice(0,4)]).
        sort((a,b) => b[1]-a[1]).
        map(o => o[0]).join('');
    if (answer[0] == '0') return '0';
    else return answer;
}