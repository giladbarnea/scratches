function extend(sup, base) {
	console.log('extend', { sup, base });
	const descriptor = Object.getOwnPropertyDescriptor(
		base.prototype, 'constructor'
	);
	base.prototype = Object.create(sup.prototype); // Person {}
	const handler = {
		construct: function (target, args) {
			console.group('construct');
			console.log({ target, args, 'this': this });
			const obj = Object.create(base.prototype);
			console.log('after obj = Object.create(base.prototype)', { obj, 'this': this });
			this.apply(target, obj, args);
			console.log('after this.apply(target, obj, args)', { obj, 'this': this });
			console.groupEnd();
			return obj;
		},
		apply: function (target, that, args) {
			console.group('apply');
			console.log({ target, that, args });
			sup.apply(that, args);
			console.log('after sup.apply(that, args)', { sup, base, that });
			base.apply(that, args);
			console.log('after base.apply(that, args)', { sup, base, that });
			console.groupEnd();
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


const Boy = extend(String, function (name) {
	this.name = name;
});

Boy.prototype.sex = 'M';

const Peter = new Boy('Peter');
// const myString = String('PeterString');
// console.log(Peter.sex);  // "M"
console.log({ Peter, 'Peter.name': Peter.name, 'Peter.sex': Peter.sex });
// console.log(myString);
