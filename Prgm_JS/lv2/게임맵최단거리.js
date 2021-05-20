function solution(maps) {
    const bfs = (x,y) => {
        let q = [[x,y]];
        let dx = [1,0,-1,0];
        let dy = [0,1,0,-1];
        
        while(q.length>0) {
            let cur = q.shift();
            for(let i=0;i<4;i++){
                let nx = cur[0]+dx[i];
                let ny = cur[1]+dy[i];
                
                if(nx>=0 && ny>=0 && nx<maps.length && ny<maps[0].length) {
                    if(maps[nx][ny] === 1) {
                        maps[nx][ny] = maps[cur[0]][cur[1]]+1;
                        q.push([nx,ny]);
                    }
                }
            }
        }
    }
    
    bfs(0,0);
    return maps[maps.length-1][maps[0].length-1] > 1 ?
            maps[maps.length-1][maps[0].length-1] : -1;
}