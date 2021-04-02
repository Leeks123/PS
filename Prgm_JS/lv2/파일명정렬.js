function fileNameSpliter(file) {
    file = file.toUpperCase();
    const head = file.match(/[A-Z\s.-]+/)[0];
    file = file.slice(head.length,);
    const number = file.match(/[0-9]+/)[0];
    file = file.slice(number.length,);
    const tail = file;

    return [
        head,number,tail
    ]
}
function solution(files) {
    return files.
    sort((a,b) => {
        const [ Ahead,Anum,Atail ] = fileNameSpliter(a);
        const [ Bhead,Bnum,Btail ] = fileNameSpliter(b);

        if(Ahead < Bhead) {
            return -1;
        } else if(Ahead === Bhead) {
            if(parseInt(Anum) < parseInt(Bnum)) {
                return -1;
            } else if(parseInt(Anum) === parseInt(Bnum)) {
                return 0;
            } else {
                return 1;
            }
        } else {
            return 1;
        }
    });

}