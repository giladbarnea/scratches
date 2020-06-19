type Element2Tag<T> = T extends HTMLInputElement ? "input" : never;

class Foo<Generic extends HTMLInputElement> {

    constructor(tag: Element2Tag<Generic>) {

    }
}

// GOOD:
const foo = new Foo("input");


// BAD:
class ChildFoo<Generic extends HTMLInputElement> extends Foo<Generic> {

    constructor() {
        super("input" as Element2Tag<Generic>);
    }
}
