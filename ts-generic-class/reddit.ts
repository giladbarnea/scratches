/* 

 // Returns an array of [key,value] tuples.
 // @example
 // objToKeyValuePairs( { pizza: true, beers: 2 } )  // [ [ "pizza", true ], [ "beers", 2 ] ]
 //
declare function objToKeyValuePairs<T, K extends keyof T>(obj: T): Array<[K, T[K]]>;

function errorsAsExpected(friends: FriendsConditional<string>) {
    let keyValuePairs = objToKeyValuePairs(friends);


    for (let [name, type] of keyValuePairs) {
        if (name === "NO_SUCH_FRIEND") {

        }
    }
}


function shouldErrorButDoesnt<T extends string>(friends: FriendsConditional<T>) {
    let keyValuePairs = objToKeyValuePairs(friends);


    for (let [name, type] of keyValuePairs) {
        if (name === "NO_SUCH_FRIEND") {

        }
    }
}
 */