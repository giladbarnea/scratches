let vet = {
    heal() {
        return {
            fluffy: true,
            type: 'mammal',
        };
    },
};
function* enumerateSingle(obj) {
    if (Array.isArray(obj)) {
        for (let x of obj) {
            yield x;
        }
    }
    else {
        for (let prop in obj) {
            if (obj.hasOwnProperty(prop)) {
                yield prop;
            }
        }
    }
}
function* enumerate(obj) {
    if (Array.isArray(obj)) {
        let i = 0;
        for (let x of obj) {
            yield [i, x];
        }
    }
    else {
        for (let prop in obj) {
            yield [prop, obj[prop]];
        }
    }
}
let dog = {
    fluffy: true,
    type: 'mammal',
};
const arr = [1, 2, 3];
for (let n of enumerateSingle(arr)) {
}
for (let prop of enumerateSingle(dog)) {
}
for (let [n, x] of enumerate(arr)) {
}
for (let [k, v] of enumerate(dog)) {
}
function getKeys(o) {
    return Object.keys(o);
}
function getValues(o) {
    return Object.values(o);
}
function getEntries(o) {
    return Object.entries(o);
}
function* entries(o) {
    for (let [k, v] of Object.entries(o))
        yield [k, v];
}
function* nativeEntries(o) {
    if (Array.isArray(o)) {
        let i = 0;
        for (let v of o) {
            yield [i, v];
            i++;
        }
        return;
    }
    for (let k in o)
        yield [k, o[k]];
}
function* nativeEntriesArr(o) {
    let i = 0;
    for (let v of o) {
        yield [i, v];
        i++;
    }
}
function* nativeEntriesObj(o) {
    for (let k in o)
        yield [k, o[k]];
}
for (let [k, v] of entries(dog)) {
}
for (let [k, v] of nativeEntries(dog)) {
}
for (let [k, v] of nativeEntries([dog, dog])) {
}
