function solution(n, words) {
    var answer = [0,0];
    let prev = words[0][0];
    words.some((word,i) => {
        if(word[0] != prev) {
            answer = [i%n+1,Math.floor(i/n)+1]
            return true;
        } else {
            prev = word[word.length-1];
        }
        if(words.slice(0,i).includes(word)) {
            answer = [i%n+1,Math.floor(i/n)+1];
            return true;
        }
    })

    return answer;
}