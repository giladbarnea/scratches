declare function noChange<T>(obj: T): T
declare function keyOf<T>(obj: T): keyof T
type KeyOf<T> = keyof T
function errorsAsExpected_1<T extends string>(friends: FriendsConditional<T>) {
	let same = noChange(friends);
	return same.noSuchFriend;
}

function errorsAsExpected_2(friends: FriendsConditional<string>) {
	let key = keyOf(friends);
	return key === "noSuchFriend"
}

// BUG? Function is equivalent to errorsAsExpected_2
function shouldErrorButDoesnt<T extends string>(friends: FriendsConditional<T>) {
	let key = keyOf(friends);
	return key === "noSuchFriend"
}
function shouldErrorButDoesnt_1<T extends Person>(person: T) {
	let key: keyof typeof person;
	return key === "radius"
}

