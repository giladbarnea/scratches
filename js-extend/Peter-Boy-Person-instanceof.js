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
	return child;
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
}

// const BoyCls = extend2(PersonCtor, BoyCtor);
BoyCtor.prototype = PersonCtor.prototype;
// BoyCls.prototype.sex = 'M';

const Peter = new BoyCtor('Peter', 13);
console.log('Peter:', {
	sex: Peter.sex,      // "M"
	name: Peter.name,    // "Peter". From handler.construct
	age: Peter.age       // 13
});
console.log('Peter instanceof:', {
	PersonCtor: Peter instanceof PersonCtor,     // true. From child.prototype = SuperCtor
	BoyCtor: Peter instanceof BoyCtor            // true
});

console.log('BoyCtor instanceof PersonCtor', BoyCtor instanceof PersonCtor); // false
console.log('PersonCtor instanceof BoyCtor', PersonCtor instanceof BoyCtor); // false
