// child extends sup
function extend2(sup, child) {
	child.prototype.constructor = sup.prototype;
	const handler = {
		// no construct == no name
		construct
	};

	// "new BoyCls"
	function construct(_, argArray) {
		/*const obj = new child;
		sup.apply(obj, argArray);    // calls PersonCtor. Sets name
		child.constructor.apply(obj, argArray); // calls BoyClass. Sets age
		return obj;
		*/

		let obj = new child(...argArray);
		let newsup = new sup(...argArray);
		obj = Object.assign(obj, newsup);
		return obj;

	}


	// @ts-ignore
	const proxy = new Proxy(child, handler);
	return proxy;
}

/*class PersonCtor {
	constructor(name) {
		///  this
		///  >>> PersonCtor {}
		this.name = name;

	}

	sayHi() {
		console.log(`Hi! My name is ${this.name}.`);
	}
}

*/
function PersonCtor(name) {
	///  this
	///  >>> PersonCtor {}
	this.name = name;
	this.sayHi = function () {
		console.log(`Hi! My name is ${this.name}.`);
	};

}

class BoyClass {
	constructor(name, age) {
		///  this
		///  >>> PersonCtor {}
		this.age = age;
	}

	sayHi() {
		console.log(`Hi! My name is ${this.name}, and I'm ${this.age}.`);
	}
}


/*function BoyClass(name, age) {
	///  this
	///  >>> PersonCtor {}
	this.age = age;
	this.sayHi = function () {
		console.log(`Hi! My name is ${this.name}, and I'm ${this.age}.`);
	};
}
*/

const BoyCls = extend2(PersonCtor, BoyClass);
// const BoyCls = BoyClass;
BoyCls.prototype.sex = 'M';

const Peter = new BoyCls('Peter', 13);
console.log('Peter:', {
	sex: Peter.sex,      // "M"
	name: Peter.name,    // "Peter". From handler.construct
	age: Peter.age       // 13
});
console.log('Peter instanceof:', {
	BoyCls: Peter instanceof BoyCls,             // true
	PersonCtor: Peter instanceof PersonCtor,     // true. From child.prototype = SuperCtor
	BoyClass: Peter instanceof BoyClass            // true
});
console.log('BoyCls instanceof:', { PersonCtor: BoyCls instanceof PersonCtor, BoyClass: BoyCls instanceof BoyClass }); // false, false
console.log('BoyClass instanceof:', { PersonCtor: BoyClass instanceof PersonCtor, BoyCls: BoyClass instanceof BoyCls }); // false, false
console.log('PersonCtor instanceof:', { BoyClass: PersonCtor instanceof BoyClass, BoyCls: PersonCtor instanceof BoyCls }); // false, false
console.log('Object.getPrototypeOf(Peter) == BoyCls.prototype:', Object.getPrototypeOf(Peter) == BoyCls.prototype); // true
Peter.sayHi();
