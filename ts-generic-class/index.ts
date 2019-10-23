/* // TEventMap<HTMLElement> = HTMLElementEventMap  = { ..., "touchstart": TouchEvent, ... }
type TEventMap<T extends HTMLElementOrWindowOrDocument> =
    T extends HTMLElement ? HTMLElementEventMap
        : T extends Window ? WindowEventMap
        : T extends Document ? DocumentEventMap
            : never;

// TEvent<HTMLElement> = ... | "touchstart" | ...
type TEvent<T extends HTMLElementOrWindowOrDocument> = keyof TEventMap<T>;

// TEventFunctionMap<HTMLElement> = { ..., "touchstart": (event: TouchEvent) => void, ... }
type TEventFunctionMap<T extends HTMLElementOrWindowOrDocument> = {
    [P in TEvent<T>]?: (event: TEventMap<T>[P]) => void;
};

type HTMLElementOrWindowOrDocument = HTMLElement | Window | Document;
type KVPairs<T> = { [K in keyof T]: [K, T[K]][] }[keyof T]; // GOOD
type HTMLKVPairs<T extends HTMLElementOrWindowOrDocument> = {
    [K in keyof T]: K extends TEvent<T> ? [K, T[K]][] : never
}[keyof T];
type KVPairsOrArr<T> =
    T extends any[] ? [number, T[number]][]
        : { [K in keyof T]: [K, T[K]][] }[keyof T];
type InferredKVPairsOrArr<T> =
    T extends (infer U)[] ? [number, U][]
        : { [K in keyof T]: [K, T[K]][] }[keyof T];

type InferredKVPairs<T> = { [K in keyof T]: T[K] extends infer U ? [K, U][] : any }[keyof T]; // GOOD


interface TMap<T> {
    [s: string]: T;
    
    [s: number]: T
}


interface Programmer<T> {
    name: string;
    age: number;
    lang: T
}

function isObject(obj): obj is object {
    return typeof obj === 'object' && !!obj;
}


// function enumerate<T>(obj: T): KVPairs<T> {
//     if (!isObject(obj))
//         return;

//     let keys = Object.keys(obj);
//     let firstKey = keys[0];
//     let firstVal = obj[firstKey];
//     return [firstKey, firstVal] as KVPairs<T>;

// }


interface Animal {
    mammal: boolean;
}

interface AnimalThings {
    bark: () => string;
}

interface Person {
    name: string;
    age: number;
}

interface PersonThings {
    converse: () => string[];
}

type PersonOrAnimal = Person | Animal;
type TEventMap2<T extends PersonOrAnimal> = T extends Person ? PersonThings : T extends Animal ? AnimalThings : never;

class AbstractClass0<T extends { name: string; age: number }> {
    foo0(something: { name: string; age: number }) {
        for (let [k, v] of enumerate(something)) { // GOOD
        
        }
    }
    
    foo1(something: T) {
        
        for (let [k, v] of enumerate(something)) { // GOOD
        
        }
    }
}

class AbstractClass1<T extends Person> {
    foo0(something: Person) {
        for (let [k, v] of enumerate(something)) { // GOOD
        
        }
    }
    
    foo1(something: T) {
        for (let [k, v] of enumerate(something)) { // GOOD
        
        }
    }
}

type Enumerated<T> =
    T extends (infer U)[] ? [number, U][]
        : T extends GenericMap<(infer U)> ? [keyof T, U][]
        : [keyof T, T[keyof T]][];

type EnumeratedNoArr<T> =
    T extends GenericMap<(infer U)> ? [keyof T, U][]
        : [keyof T, T[keyof T]][];

type EnumeratedInferred<T> = [keyof T, T[keyof T] extends infer U ? U : never][]
type EnumeratedSimple<T> = [keyof T, T[keyof T]][];


type GenericMap<T> = { [K: string]: T }


// type GetHTMLEventNames<T> = keyof GetHTMLElementEventMap<T>;
// type GetHTMLEventNameFunctionMap<T> = { [K in GetHTMLEventNames<T>]: (event: GetHTMLElementEventMap<T>[K]) => any | null }
// type HTMLElementEventMap2 = GetHTMLElementEventMap<HTMLElement>;
// type HTMLEventNames = keyof HTMLElementEventMap;
// type HTMLEventNames2 = keyof GetHTMLElementEventMap<HTMLElement>;
// type HTMLEventNameFunctionMap = { [K in HTMLEventNames]: (event: HTMLElementEventMap[K]) => any | null }
// type HTMLEventNameFunctionMap2 = { [K in HTMLEventNames2]: (event: HTMLElementEventMap[K]) => any | null }
// type HTMLEventNameFunctionMap3 = { [K in HTMLEventNames]: (event: HTMLElementEventMap2[K]) => any | null }
// type HTMLEventNameFunctionMap4 = { [K in HTMLEventNames2]: (event: HTMLElementEventMap2[K]) => any | null }
// type HTMLEventNameFunctionMap5 = { [K in GetHTMLEventNames<HTMLElement>]: (event: HTMLElementEventMap[K]) => any | null }
// type HTMLEventNameFunctionMap6<T = HTMLElement> = { [K in GetHTMLEventNames<T>]: (event: HTMLElementEventMap[K]) => any | null }
// type HTMLEventNameFunctionMap7<T extends HTMLElement> = { [K in GetHTMLEventNames<T>]: (event: HTMLElementEventMap[K]) => any | null }


declare function isGetEventMapString<T>(obj: EventMapIfString<string>): obj is EventMapIfString<string>;


 */