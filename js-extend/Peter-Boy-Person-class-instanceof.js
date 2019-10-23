function PersonCtor(name) {
	this.name = name;

	this.sayHi = function () {
		console.log(`Hi! My name is ${this.name}.`);
	};
}

class BoyCtor {
	constructor(name, age) {
		this.age = age;
		return new Proxy(this, {
			get(target, p, receiver) {
				if (p === "prototype") debugger;
				return target[p];
			}
		});
	}
}

const Peter = new BoyCtor('Peter', 13);
console.log(Peter instanceof PersonCtor);
