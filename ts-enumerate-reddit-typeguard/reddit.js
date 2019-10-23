class MyDict {
    constructor(obj) {
        Object.assign(this, obj);
    }
    *items() {
        for (let k in this) {
            yield [k, this[k]];
        }
    }
    *essohbeeItems() {
        const proxy = this;
        for (const k in proxy) {
            yield [k, proxy[k]];
        }
    }
}
function mydict(obj) {
    return new MyDict(obj);
}
class FufrimDict {
    constructor(_items) {
        this._items = _items;
    }
    *items() {
        for (let k in this._items) {
            yield [k, this._items[k]];
        }
    }
}
function fufrimdict(obj) {
    return new FufrimDict(obj);
}
const pizza = { origin: 'Italy', type: 'main' };
const crepe = { origin: 'France', type: 'dessert' };
const foodRatings = { pizza: [pizza, 10], crepe: [crepe, 8] };
const foodDict = mydict(foodRatings);
for (let [name, [food, rating]] of foodDict.essohbeeItems()) {
}
