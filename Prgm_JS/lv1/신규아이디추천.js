function solution(new_id) {
    const phase1 = (id) => id.toLowerCase();
    const phase2 = (id) => id.replace(/[^a-z0-9_\-.]/g,'');
    const phase3 = (id) => id.replace(/(\.)\1+/g,'.');
    const phase4 = (id) => id.replace(/^\.|\.$/g,'');
    const phase5 = (id) => id==='' ? 'a' : id;
    const phase6 = (id) => {
        if (id.length > 15) {
            return phase4(id.slice(0,15))
        }
        return id;
    };
    const phase7 = (id) => {
        if (id.length <= 2) {
            id +=id[id.length-1].repeat(3 - id.length)
        }
        return id;
    }
    
    return phase7(phase6(phase5(phase4(phase3(phase2(phase1(new_id)))))));
}