// https://stackoverflow.com/a/10430875
const Person = function (name) {
	this.name = name;
	this.type = 'human';
};


class RobotClass {
	constructor(name) {
		console.log(arguments);
		Person.apply(this, arguments);
		this.type = 'robot';

	}
}

Person.prototype.info = function () {
	console.log("Name:", this.name, "Type:", this.type);
};
const Robot = function (name) {
	console.log(arguments);
	Person.apply(this, arguments);
	this.type = 'robot';
};
// RobotClass.prototype = new Proxy()
// Object.defineProperty(RobotClass, 'prototype', Person.prototype);
Robot.prototype = Person.prototype;        // Set prototype to Person's
// RobotClass.constructor = Person;        // Set prototype to Person's
// Robot.prototype = Object.create(Person.prototype);        // Set prototype to Person's
// Robot.prototype.constructor = Robot;   // Set constructor back to Robot

let peter = new Person("Peter");
let r2d2 = new Robot("R2D2");
// let r2d2 = new RobotClass("R2D2");

peter.info();
// Name: Bob Type: human

r2d2.info();
// Name: R2D2 Type: r2d2
console.log({
	'r2d2 instanceof Person': r2d2 instanceof Person, // true
	'peter instanceof Person': peter instanceof Person // true
});
