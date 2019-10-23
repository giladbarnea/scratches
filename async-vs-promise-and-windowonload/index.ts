function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

window.isLoaded = false;
window.onload = () => {
    window.isLoaded = true;
};
window.promiseLoaded = async function () {
    console.log('window.promiseLoaded()');
    if (this.isLoaded)
        return true;
    let count = 0;
    while (!this.isLoaded) {
        if (count >= 2000) {
            if (count === 2000)
                console.trace(`window.promiseLoaded() count: ${count}. Waiting 200ms, warning every 1s.`);
            else if (count % 5 === 0)
                console.warn(`window.promiseLoaded() count: ${count}. Waiting 200ms, warning every 1s.`);
            await wait(200);
        } else {
            await wait(5);
        }
        
        count++;
    }
    console.log('window.promiseLoaded() returning true');
    this.isLoaded = true;
    return true;
};

async function promiseWindowLoaded(): Promise<void> {
    const loaded = new Promise(resolve => window.onload = () => resolve('hehe'));
    console.log('promiseWindowLoaded awaiting loaded...');
    const result = await loaded;
    console.log('promiseWindowLoaded done awaiting loaded');
}
