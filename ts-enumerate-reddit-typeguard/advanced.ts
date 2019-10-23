function f<T>(x: T): T extends true ? string : number;
function f(x) {
    if (typeof x !== 'number') return 'hi';
    else return 5;
}

// Type is 'string | number
let x = f(Math.random());
console.log(x);

interface Foo {
    propA: boolean;
    propB: boolean;
}

type Tfoo<T> = T extends (infer R) ? R : Foo;

function foo<T>(x: T): Tfoo<T>;

function foo(x) {
    // Has type 'U extends Foo ? string : number'
    if (typeof x === 'number') return {};
    else return {};
}

let y = foo(() => {
    throw new Error('lol');
});

type FunctionPropertyNames<T> = { [K in keyof T]: T[K] extends Function ? K : never };

interface Part {
    id: number;
    name: string;
    subparts: Part[];

    updatePart(newName: string): void;
}

type T40 = FunctionPropertyNames<Part>[keyof Part];
type Unpacked<T> = T extends (infer U)[]
    ? U
    : T extends (...args: any[]) => infer U
    ? U
    : T extends Promise<infer U>
    ? U
    : T;
