function extend(sup, base) {
	const descriptor = Object.getOwnPropertyDescriptor(
		base.prototype, 'constructor'
	);
	base.prototype = Object.create(sup.prototype); // Person {}
	const handler = {
		construct: function (target, args) {
			const obj = Object.create(base.prototype);
			this.apply(target, obj, args);
			return obj;
		},
		apply: function (target, that, args) {
			sup.apply(that, args);
			base.apply(that, args);
		}
	};
	const proxy = new Proxy(base, handler);
	descriptor.value = proxy;
	Object.defineProperty(base.prototype, 'constructor', descriptor);
	return proxy;
}


function Person(name) {
	this.name = name;
}

function Base(name, age) {
	this.age = age;
}

const Boy = extend(Person, Base);

Boy.prototype.sex = 'M';

const Peter = new Boy('Peter', 13);
console.log(Peter.sex);  // "M"
console.log(Peter.name); // "Peter"
console.log(Peter.age);  // 13
console.log({ 'Peter instanceof Boy': Peter instanceof Boy }); // true
