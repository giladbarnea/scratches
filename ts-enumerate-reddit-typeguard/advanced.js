function f(x) {
    if (typeof x !== 'number')
        return 'hi';
    else
        return 5;
}
let x = f(Math.random());
console.log(x);
function foo(x) {
    if (typeof x === 'number')
        return {};
    else
        return {};
}
let y = foo(() => {
    throw new Error('lol');
});
