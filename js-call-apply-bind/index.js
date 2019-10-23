const obj = { num: 2 };
// **  call: sets 'this' via first arg, then ...args
const increase = function (extra, moreExtra) {return (this.num + 1) * extra * moreExtra;};
const increased = increase.call(obj, 1, 1);
console.log(increased); // (2+1) * 1 * 1 == 3

// **  bind: sets 'this' explicitly, then ...args
const bound = increase.bind(obj);
console.dir(bound);
console.log(bound(2, 100)); // (2+1) * 2 * 100 == 600

// **  apply: like 'call', only with [...args]
const applied = increase.apply(obj, [3, 10]);
console.log(applied); // (2+1) * 3 * 10 == 90
