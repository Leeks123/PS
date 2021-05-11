function solution(dirs) {
    let move = {
        'U':[1,0],'D':[-1,0],'R':[0,1],'L':[0,-1]
    };
    let visited = [];
    let pos = [0,0];
    dirs.split('').forEach((v) => {
        let nx = pos[0]+move[v][0];
        let ny = pos[1]+move[v][1];
        if(nx>=-5 && nx <= 5 && ny>=-5 && ny<=5) {
            if(!visited.includes((pos[0]+nx)/2+' '+(pos[1]+ny)/2)){
                visited.push((pos[0]+nx)/2+' '+(pos[1]+ny)/2);   
            }
            pos = [nx,ny];
        }
    });
    console.log(visited);
    return visited.length;
}