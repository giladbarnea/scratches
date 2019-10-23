interface Person {
    name: string;
}

function errorsAsExpected(person: Person) {
    let key: keyof typeof person = "name";
    
    // This condition will always return 'false'
    // since the types '"name"' and '"radius"' have no overlap.ts(2367)
}

declare function isPerson(person: Person): person is Person;

function shouldErrorButDoesnt<T extends Person>(person: T): boolean | string {
    let key: keyof typeof person = "radius";
    if (isPerson(person))
        return key === "radius";    // no error despite being equivalent to "errorsAsExpected".
    else
        return "hi";
}

interface AnotherPerson extends Person {
    radius: string;
}

let anotherPerson: AnotherPerson = {radius: "5", name: "yosi"};
console.log(shouldErrorButDoesnt(anotherPerson));

errorsAsExpected(anotherPerson);
