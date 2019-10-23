class Dict {
	constructor(obj) {
		Object.assign(this, obj);
	}

	hi() {
		console.log('hi');
	}
}

let obj = { key: 'value!' };
let objhi = { hi() {console.log('hi');} };
let objwhat = { what() {console.log('what');} };
Object.assign(obj, Object, objhi, objwhat);
obj = { ...obj, hello() {console.log('hello');} };
console.log(obj);
let dict = new Dict({ dictkey: 'dictvalue!' });
console.log(dict.dictkey);
