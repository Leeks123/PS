function solution(brown, yellow) {
    let blocks = brown+yellow;
    let height = 1;
    while(true){
        if((blocks/height-2)*(height-2) == yellow) {
            break;
        }
        height++;
    }
    return [blocks/height,height]
}