interface Person {
	name: string
}
interface Dog {
	fluffy: boolean
}

interface Friends {
	joe: Person;
	max: Dog;
}

type FriendsConditional<T> = T extends string ? Friends : never;

function errorsAsExpected_0<T extends string>(arg: FriendsConditional<T>) {
	return arg.noSuchFriend
}

