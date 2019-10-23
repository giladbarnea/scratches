class MyDict<T> {
    constructor(obj: T) {
        Object.assign(this, obj);
    }

    // TODO: This can't be the simplest way to do it?
    *items(): IterableIterator<[Extract<keyof T, string>, T[Extract<keyof T, string>]]> {
        for (let k in this) {
            yield <[Extract<keyof T, string>, T[Extract<keyof T, string>]]>(<unknown>[k, this[k]]);
        }
    }

    *essohbeeItems(): IterableIterator<[string, T[keyof T]]> {
        const proxy = (this as unknown) as T;
        for (const k in proxy) {
            yield [k, proxy[k]];
        }
    }
}

function mydict<T>(obj: T): MyDict<T> {
    // to avoid using "new"
    return new MyDict<T>(obj);
}

class FufrimDict<T> {
    // We use constructor initialiser to init a new property for the class
    // I did this because applying it to the this of the instance does not work fantasticly with typescript
    constructor(private _items: T) {}

    // Typescript is really good at inferring the actual type
    *items() {
        for (let k in this._items) {
            yield [k, this._items[k]] as const;
        }
    }
}

function fufrimdict<T>(obj: T) {
    // to avoid using "new"
    return new FufrimDict<T>(obj);
}

// USAGE
type FoodType = 'main' | 'dessert';

interface Food {
    type: FoodType;
    origin: string;
}

const pizza: Food = { origin: 'Italy', type: 'main' };
const crepe: Food = { origin: 'France', type: 'dessert' };
const foodRatings: { [name: string]: [Food, number] } = { pizza: [pizza, 10], crepe: [crepe, 8] };

const foodDict = mydict(foodRatings);
for (let [name, [food, rating]] of foodDict.essohbeeItems()) {
}
