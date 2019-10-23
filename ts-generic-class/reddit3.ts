type StringConditional<T> = T extends string ? string : never;

function conditional<T extends string>(arg: StringConditional<T>) {
	return arg === false;
}

