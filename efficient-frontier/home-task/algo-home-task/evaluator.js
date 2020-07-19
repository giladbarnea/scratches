'use strict'
// The bid price is what buyers are willing to pay for it.
// The ask price is what sellers are willing to take for it.
// If you are selling a stock, you are going to get the bid price.
// if you are buying a stock you are going to get the ask price.
// a seller asks for X, but gets the highest bid.
// a buyer offers (bids).
let datafile;
let ordersfile;
for (let arg of process.argv) {
    if (arg.startsWith('--data')) {
        datafile = arg.substr(7);
    } else if (arg.startsWith('--orders')) {
        ordersfile = arg.substr(9);
    }
}
const states = require(datafile)
const trades = require(ordersfile)

const [ A, B ] = [ { cash: 0, amount: 0 }, { cash: 0, amount: 0 } ]


let lastTrade

while (trades.length) {
    let { time, actions } = trades.shift()
    if (time < lastTrade + 30 * 1000) {
        throw new Error(`invalid trade! Wait at least 30 seconds between trades... (you waited only ${(time - lastTrade)/1000}s)`)
    }
    console.group(new Date(time));
    lastTrade = time

    const {
        assetA: {
            ask: a_ask, bid: a_bid
        }, assetB: {
            ask: b_ask, bid: b_bid
        }
    } = states[time]
    let a_title = 'A';
    let b_title = 'B';

    ///If I'm *buying*,
    // I'll have *less* cash ↓, but
    // amount ↑ goes *up*.
    // I'm hoping the price is low.
    if (actions.includes('buyA')) {
        A.amount += 1
        A.cash -= a_ask
        console.log(`Bought A for ${a_ask}$ (cash: ↓ | amount: ↑)`);
        a_title = `A - ${a_ask}$ (bought)`
    }
    if (actions.includes('buyB')) {
        B.amount += 1
        B.cash -= b_ask
        console.log(`Bought B for ${b_ask}$ (cash: ↓ | amount: ↑)`);
        b_title = `B - ${b_ask}$ (bought)`
    }
    /// If I'm *selling*,
    // I have *more* cash ↑, but
    // amount ↓ goes *down*.
    // I'm hoping the price is high.
    if (actions.includes('sellB')) {
        B.amount -= 1
        B.cash += b_bid
        console.log(`Sold B for ${b_bid}$ (cash: ↑ | amount: ↓)`);
        b_title = `B + ${b_bid}$ (sold)`
    }
    if (actions.includes('sellA')) {
        A.amount -= 1
        A.cash += a_bid
        console.log(`Sold A for ${a_bid}$ (cash: ↑ | amount: ↓)`);
        a_title = `A + ${a_bid}$ (sold)`
    }

    /// Calculate P&L
    let a_pnl;
    if (A.amount > 0) {
        // I've *bought* more over time.
        // profit (cash) is low, but
        // amount is positive.
        // To compensate for my lack of cash,
        // I'm hoping the asset is very expensive right now
        // and that I have lots of it.

        // *In other words*:
        // If I've bought a lot, and
        // now the buying price is very high,
        // it's best if I'd bought a lot when the price
        // was low, and now my share is worth a lot
        a_pnl = A.cash + (A.amount * a_bid);
    } else {
        // I've *sold* more over time.
        // profit (cash) is high, but
        // amount is negative.
        // To minimize loss,
        // I'm hoping the asset is very cheap,
        // and that I have as close to 0 as possible.

        // *In other words*:
        // If I've sold a lot, and
        // now the selling price is very high,
        // it's like I shorted a booming stock.
        a_pnl = A.cash + (A.amount * a_ask);
    }

    let b_pnl;
    if (B.amount > 0) {
        b_pnl = B.cash + B.amount * b_bid;
    } else {
        b_pnl = B.cash + B.amount * b_ask;
    }
    let table = {
        cash: {},
        amount: {},
        "P&L": {}
    };
    table.cash[a_title] = A.cash + "$";
    table.cash[b_title] = B.cash + "$";
    table.cash["Total"] = A.cash + B.cash + "$";
    table.amount[a_title] = A.amount;
    table.amount[b_title] = B.amount;
    table.amount["Total"] = A.amount + B.amount;
    table["P&L"][a_title] = a_pnl + '$';
    table["P&L"][b_title] = b_pnl + '$';
    table["P&L"]["Total"] = a_pnl + b_pnl + '$';

    console.table(table)
    console.log('\n');
    console.groupEnd();
    // console.log(`${time}: ${a_pnl} + ${b_pnl} = ${a_pnl + b_pnl}`)
}

