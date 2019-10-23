console.log("hi");
function getFish() {
    return {
        swim: () => console.log(`I'm swimming!`),
        layEggs: () => console.log(`I'm laying eggs!`)
    };
}
function getRandomPet() {
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
    let pet = getRandomPet();
    if (pet.swim) {
        pet.swim();
    }
    else if (pet.fly) {
        pet.fly();
    }
};
const secondWay = () => {
    let pet = getRandomPet();
    if (pet.swim) {
        pet.swim();
    }
    else {
        pet.fly();
    }
};
secondWay();
function isFish(pet) {
    return pet.swim !== undefined;
}
const thirdWay = () => {
    let pet = getRandomPet();
    if (isFish(pet)) {
        pet.swim();
    }
    else {
        pet.fly();
    }
};
