/**
 * @param {character[][]} grid
 * @return {number}
 */
 var numIslands = function(grid) {
    const bfs = (grid,x,y) => {
        if(grid[x][y]!=='1') return 0;
        
        let q = [[x,y]];
        grid[x][y] = '-1';
        
        let dx = [0,0,1,-1];
        let dy = [1,-1,0,0];
        
        while(q.length > 0){
            let [checkX,checkY] = q.shift();
            for(let i=0;i<4;i++){
                const nx = dx[i]+checkX;
                const ny = dy[i]+checkY;
                if(nx>=0 && nx<grid.length && ny>=0 && grid[0].length && grid[nx][ny] === '1') {
                    grid[nx][ny] = '-1';
                    q.push([nx,ny]);      
                }
            }
        }
        
        return 1;
    }  
    let answer = 0;
    for(let i=0;i<grid.length;i++){
        for(let j=0; j<grid[0].length;j++) {
            answer+= bfs(grid,i,j);
        }
    }
    return answer;
};