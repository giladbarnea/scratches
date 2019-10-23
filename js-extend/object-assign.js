class Int extends Number {


	constructor(value) {
		super(value);
	}

	valueOf() {

		console.log('valueOf', { 'this': this, arguments, 'super.valueOf.callee': super.valueOf.callee });
		debugger;
		return super.valueOf();
	}

	toString(radix) {
		console.log('toString', { 'this': this, radix });
		return super.toString();
	}
}


/*const Int = function (value) {
	this.value = value;
	Number.apply(this, arguments);
};
Int.prototype = Object.create(Number.prototype);
Int.prototype.constructor = Int;
*/


// let IntFunction = Number;


// Int = Object.assign(Number);


// let Int = _.extend(Number, foo);

/*Object.prototype.extend = function (obj) {
	for (var i in obj) {
		if (obj.hasOwnProperty(i)) {
			this[i] = obj[i];
		}
	}
};
*/
// Object.assign(Int, Number);
// Int.prototype.extend(foo);
// Int.prototype = Number.prototype;

function int(value) {
	let number = Int(value);


	return number;
}

// GOOD
/*Object.assign(Int.prototype, {
	what() {
		console.log('what');
	}
});
*/


// GOOD
/*Int.prototype = Object.assign(Int.prototype, {
	what() {
		console.log('what');
	}
});
*/

// GOOD
/*Int.prototype.what = function () {
	console.log('what', this);
};
*/


// GOOD
/*Object.defineProperty(Int.prototype, 'what', {
	value() {
		console.log('what', this);
	}
});
*/


// let i = Int(5);
let i5 = new Int(5);
let i0 = new Int(0);
let num = Number(15);
console.log({ i5, i0, 'i5/i0': i5 / i0 });
console.log({ num });

try {
	i5.what();
} catch (e) {
	console.warn(e);
}
try {
	num.what();
} catch (e) {
	console.warn(e);
}


