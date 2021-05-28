function bfs(graph, start, visited) {
    let q = [start];
    visited[start] = true;

    while(q.length>0){
        let v = q.shift();
        console.log(v);
        graph[v].forEach(node => {
            if(!visited[node]) {
                q.push(node);
                visited[node] = true;
            }
        })
    }
}

function solve(){
    let graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    const visited = new Array(9).fill(false);

    bfs(graph,1,visited);
}