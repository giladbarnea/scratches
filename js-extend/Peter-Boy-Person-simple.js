// child extends sup
function extend2(sup, child) {
	//////////////////////////////////////////////////////////////
	// child  ==  BoyCtor                                       //
	// sup  ==  PersonCtor                                      //
	/// Peter instanceof PersonCtor  ==  false
	/// child.prototype.constructor  ==  BoyCtor                //
	// sup.prototype.constructor  ==  PersonCtor                //
	// Can do:  new sup( "shlomo" )                             //
	//          new sup.prototype.constructor( "shlomo" )       //
	//          >>> PersonCtor { name: "shlomo" }               //
	//          new child( "shlomo", 15 )                       //
	//          new child.prototype.constructor( "shlomo", 15 ) //
	///         >>> BoyCtor { age: 15 }                         //
	//////////////////////////////////////////////////////////////
	child.prototype = sup.prototype;
	//////////////////////////////////////////////////////////////////////////
	/// Peter instanceof PersonCtor  ==  true                       //
	/// child.prototype.constructor  ==  PersonCtor( name )         //
	//  Can do:  new child( "shlomo", 15 )                          //
	//           new child.prototype.constructor( "shlomo" )        //
	///          >>> PersonCtor { name: "shlomo" }                  //
	//////////////////////////////////////////////////////////////////////////
	const handler = {
		// no construct == no name
		construct
	};

	// "new BoyCls"
	function construct(_, argArray) {
		/////////////////////////////////////////////////////
		// target  ==  BoyCtor                             //
		// target.prototype.constructor  ==  PersonCtor    //
		/////////////////////////////////////////////////////
		////////////////////////////////////////////////////////
		// child  ==  BoyCtor                                 //
		// child.prototype.constructor  ==  PersonCtor        //
		// sup.prototype.constructor  ==  PersonCtor          //
		// sup.prototype  ==  child.prototype                 //
		// can use sup instead of child here, doesn't matter  //
		// Can do:  new child( "shlomo", 15 )                 //
		//          / >>> BoyCtor { age: 15 }                 //
		//          new child.prototype.constructor( "shlomo" )/
		//           >>> PersonCtor { name: "shlomo" }        //
		////////////////////////////////////////////////////////
		// const obj = Object.create(child.prototype);
		const obj = new child;
		////////////////////////////////////////////////////////
		//  obj.constructor == PersonCtor                      //
		//  obj.constructor  ==  child.prototype.constructor   //
		///  obj                                                //
		///  >>> PersonCtor {}                                 //
		//  Can do: new obj.constructor( "shlomo" )            //
		//            >>> PersonCtor { name: "shlomo" }        //
		//  equiv: new child.prototype.constructor( "shlomo" ) //
		////////////////////////////////////////////////////////
		sup.apply(obj, argArray);    // calls PersonCtor. Sets name
		///////////////////////////////////////
		///  obj                             //
		///  >>> PersonCtor {name: "Peter"}  //
		///////////////////////////////////////
		child.apply(obj, argArray); // calls BoyCtor. Sets age
		////////////////////////////////////////////////
		///  obj                                      //
		///  >>> PersonCtor {name: "Peter", age: 13}  //
		////////////////////////////////////////////////
		return obj;
	}


	// @ts-ignore
	const proxy = new Proxy(child, handler);
	return proxy;
}


function PersonCtor(name) {
	///  this
	///  >>> PersonCtor {}
	this.name = name;

	this.sayHi = function () {
		console.log(`Hi! My name is ${this.name}.`);
	};
}

function BoyCtor(name, age) {
	///  this
	///  >>> PersonCtor {}
	this.age = age;
	this.sayHi = function () {
		console.log(`Hi! My name is ${this.name}, and I'm ${this.age}.`);
	};
	this.sayBye = function () {
		console.log(`Goodbye! My name is ${this.name}, and I'm ${this.age}.`);
	};
}

const BoyCls = extend2(PersonCtor, BoyCtor);
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
	BoyCtor: Peter instanceof BoyCtor            // true
});
console.log('BoyCls instanceof:', { PersonCtor: BoyCls instanceof PersonCtor, BoyCtor: BoyCls instanceof BoyCtor }); // false, false
console.log('BoyCtor instanceof:', { PersonCtor: BoyCtor instanceof PersonCtor, BoyCls: BoyCtor instanceof BoyCls }); // false, false
console.log('PersonCtor instanceof:', { BoyCtor: PersonCtor instanceof BoyCtor, BoyCls: PersonCtor instanceof BoyCls }); // false, false
console.log('Object.getPrototypeOf(Peter) == BoyCls.prototype:', Object.getPrototypeOf(Peter) == BoyCls.prototype); // true
Peter.sayBye();
