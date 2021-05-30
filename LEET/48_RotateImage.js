/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
 var rotate = function(matrix) {
    let answer = [];
    for(let i=0;i<matrix.length;i++){
        let row = [];
        for(let j=0;j<matrix.length;j++){
            row.unshift(matrix[j][i]);
        }
        answer.push(row);
    }
    for(let i=0;i<matrix.length;i++){
        matrix[i] = answer[i];
    }
};