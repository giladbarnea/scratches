const obj = { num: 2 };
const increase = function (extra: number, moreExtra: number): number {
    return (this.num + 1) * extra * moreExtra;
};
// **  call: sets 'this' via first arg, then ...args
const increased: number = increase.call(obj, 1, 1);
console.log(increased); // (2+1) * 1 * 1 == 3

// **  bind: sets 'this' explicitly, then ...args
const bound: (extra: number, moreExtra: number) => number = increase.bind(obj);
console.dir(bound);
console.log(bound(2, 100)); // (2+1) * 2 * 100 == 600

// **  apply: like 'call', only with [...args]
const applied: number = increase.apply(obj, [3, 10]);
console.log(applied); // (2+1) * 3 * 10 == 90
