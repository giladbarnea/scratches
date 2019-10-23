interface Vet {
    heal(): Animal;
}

let vet: Vet = {
    heal(): Animal {
        return {
            fluffy: true,
            type: 'mammal',
        };
    },
};
function enumerateSingle<T>(obj: T[]): IterableIterator<T>;
function enumerateSingle<T>(obj: T): IterableIterator<keyof T>;
function* enumerateSingle(obj) {
    if (Array.isArray(obj)) {
        for (let x of obj) {
            yield x;
        }
    } else {
        for (let prop in obj) {
            if (obj.hasOwnProperty(prop)) {
                yield prop;
            }
        }
    }
}
function enumerate<T>(obj: T[]): IterableIterator<[number, T]>;
function enumerate<T>(obj: T): IterableIterator<[keyof T, T[keyof T]]>;
function* enumerate(obj) {
    if (Array.isArray(obj)) {
        let i: number = 0;
        for (let x of obj) {
            yield [i, x];
        }
    } else {
        for (let prop in obj) {
            yield [prop, obj[prop]];
        }
    }
}

type AnimalType = 'mammal' | 'reptile';

interface Animal {
    fluffy: boolean;
    type: AnimalType;
}

let dog: Animal = {
    fluffy: true,
    type: 'mammal',
};
const arr: number[] = [1, 2, 3];
for (let n of enumerateSingle(arr)) {
}
for (let prop of enumerateSingle(dog)) {
}
for (let [n, x] of enumerate(arr)) {
}
for (let [k, v] of enumerate(dog)) {
}
function getKeys<T>(o: T): Array<keyof T> {
    return <Array<keyof T>>Object.keys(o);
}

function getValues<T>(o: T): Array<T[keyof T]> {
    return <Array<T[keyof T]>>Object.values(o);
}

function getEntries<T>(o: T): [keyof T, T[keyof T]][] {
    return <Array<[keyof T, T[keyof T]]>>Object.entries(o);
}

function* entries<T>(o: T): IterableIterator<[keyof T, T[keyof T]]> {
    for (let [k, v] of <Array<[keyof T, T[keyof T]]>>Object.entries(o)) yield [k, v];
}
function nativeEntries<T>(
    o: T,
): T extends any[] ? IterableIterator<[number, T]> : IterableIterator<[keyof T, T[keyof T]]>; // GOOD (equiv)
// function nativeEntries<T>(o: T): IterableIterator<T extends any[] ? [number, T] : [keyof T, T[keyof T]]> // GOOD (equiv)
function* nativeEntries(o) {
    if (Array.isArray(o)) {
        let i = 0;
        for (let v of o) {
            yield [i, v];
            i++;
        }
        return;
    }
    for (let k in o) yield [k, o[k]];
}

function* nativeEntriesArr<T>(o: T[]): IterableIterator<[number, T]> {
    let i = 0;
    for (let v of o) {
        yield [i, v];
        i++;
    }
}

function* nativeEntriesObj<T>(o: T): IterableIterator<[keyof T, T[keyof T]]> {
    for (let k in o) yield [k, o[k]];
}
for (let [k, v] of entries(dog)) {
    // 1: k = fluffy, v = true,
    // 2: k = type, v = "mammal"
}

for (let [k, v] of nativeEntries(dog)) {
}
for (let [k, v] of nativeEntries([dog, dog])) {
}
