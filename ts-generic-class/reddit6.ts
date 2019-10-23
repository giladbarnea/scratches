interface Person {
    name: string;
}

function errorsAsExpected(person: Person){
    let key: keyof typeof person;
    return key === "radius";    
    // This condition will always return 'false'
    // since the types '"name"' and '"radius"' have no overlap.ts(2367)
}


function shouldErrorButDoesnt<T extends Person>(person: T){
    let key: keyof typeof person;
    return key === "radius";    // no error despite being equivalent to "errorsAsExpected".
}