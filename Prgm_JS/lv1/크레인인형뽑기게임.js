function solution(board, moves) {
    let answer = 0;
    let size = board.length;
    let basket = [];
    
    function pickItem(move) {
        for(let i=0; i<size;i++){
            if(board[i][move-1] == 0){
                continue
            } else {
                let picked = board[i][move-1];
                board[i][move-1] = 0;
                return picked
            }
        }
        return 0;
    }
    function putToBasket(item) {
        if (item==0) return;
        if(item == basket[basket.length-1]) {
            basket.pop();
            answer+=2;
        } else {
            basket.push(item);
        }
    }
    
    moves.forEach(move => {
        let item = pickItem(move);
        putToBasket(item);
    }); 
    
    return answer;
}