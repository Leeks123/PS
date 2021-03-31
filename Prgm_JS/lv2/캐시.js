function solution(cacheSize, cities) {
    let cache = {};
    let execTime = 0;
    cities
        .map((city) => city.toLowerCase())
        .forEach((city,i) => {
            if(Object.keys(cache).includes(city)) { // hit
                cache[city] = i;
                execTime+=1;
            } else { // miss
                if(Object.keys(cache).length < cacheSize) { // cache not full
                    cache[city] = i;
                } else { // cache full
                    if(cacheSize === 0) {
                        execTime+=5;
                        return;
                    }
                    let lruTime = Object.values(cache).sort((a,b) => a-b)[0];
                    let lruCity = Object.keys(cache).filter((v) => cache[v] === lruTime)[0];
                    delete cache[lruCity];
                    cache[city] = i;
                }
                execTime+=5;
            }
        });
    return execTime;
}