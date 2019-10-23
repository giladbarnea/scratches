interface Bird {
	fly();

	layEggs();
}

interface Fish {
	swim();

	layEggs();
}
console.log("hi");
function getFish(): Fish {
	return {
		swim: () => console.log(`I'm swimming!`),
		layEggs: () => console.log(`I'm laying eggs!`)
	};
}

function getRandomPet(): Fish | Bird {
	if (Math.random() < 0.5)
		return {
			swim: () => console.log(`I'm swimming!`),
			layEggs: () => console.log(`I'm laying eggs!`)
		};
	return {
		fly: () => console.log(`I'm flying!`),
		layEggs: () => console.log(`I'm laying eggs!`)
	};
}

const oneWay = () => {
	// BAD
	let pet = getRandomPet();

	// Each of these property accesses will cause an error
	if (pet.swim) {
		pet.swim();
	} else if (pet.fly) {
		pet.fly();
	}
};
const secondWay = () => {
	// GOOD
	let pet = getRandomPet();

	if ((<Fish>pet).swim) {
		(<Fish>pet).swim();
	} else {
		(<Bird>pet).fly();
	}
};
secondWay();

function isFish(pet: Fish | Bird): pet is Fish {
	return (<Fish>pet).swim !== undefined;
}

const thirdWay = () => {
	// equivalent to secondWay. GOOD
	// Both calls to 'swim' and 'fly' are now okay.
	let pet = getRandomPet();

	if (isFish(pet)) {
		pet.swim();
	} else {
		pet.fly();
	}
};
