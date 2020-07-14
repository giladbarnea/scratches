'use strict'
// The bid price is what buyers are willing to pay for it.
// The ask price is what sellers are willing to take for it.
// If you are selling a stock, you are going to get the bid price.
// if you are buying a stock you are going to get the ask price.
// a seller asks for X, but gets the highest bid.
// a buyer offers (bids).
const states = require('./data.json')
const trades = require('./output.json')

const [ A, B ] = [ { cash: 0, demand: 0 }, { cash: 0, demand: 0 } ]

let lastTrade

while (trades.length) {
    let { time, actions } = trades.shift()
    if (time < lastTrade + 30 * 1000) {
        throw new Error(`invalid trade! Wait at least 30 seconds between trades... (${time - lastTrade})`)
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
    // I have *less* cash, but
    // demand goes *up*.
    /// If I'm *selling*,
    // I have *more* cash, but
    // demand goes *down*.
    if (actions.includes('buyA')) {
        A.demand += 1
        A.cash -= a_ask
        console.log(`Baught A for ${a_ask}$ (cash: ↓ | demand: ↑)`);
        a_title = `A - ${a_ask}$ (baught)`
    }
    if (actions.includes('sellB')) {
        // when someone sells B,
        // owner of B got whatever the buyer offered (bid).
        B.demand -= 1
        B.cash += b_bid
        console.log(`Sold B for ${b_bid}$ (cash: ↑ | demand: ↓)`);
        b_title = `B + ${b_bid}$ (sold)`
    }
    if (actions.includes('sellA')) {
        // when someone sells A,
        // owner of A gets the available bid for A.
        A.demand -= 1
        A.cash += a_bid
        console.log(`Sold A for ${a_bid}$ (cash: ↑ | demand: ↓)`);
        a_title = `A + ${a_bid}$ (sold)`
    }
    if (actions.includes('buyB')) {
        // when someone buys B,
        // the new owner of B says goodbye to whatever price the seller asked.
        B.demand += 1
        B.cash -= b_ask
        console.log(`Baught B for ${b_ask}$ (cash: ↓ | demand: ↑)`);
        b_title = `B - ${b_ask}$ (baught)`
    }

    /// Calculate P&L
    let a_pnl;
    if (A.demand > 0) {
        // I BAUGHT more over time (commulivately)
        a_pnl = A.cash + (A.demand * a_bid);
    } else {
        // I SOLD more over time (commulivately)
        a_pnl = A.cash + (A.demand * a_ask);
    }

    let b_pnl;
    if (B.demand > 0) {
        b_pnl = B.cash + B.demand * b_bid;
    } else {
        b_pnl = B.cash + B.demand * b_ask;
    }
    let table = {
        cash: {},
        demand: {},
        "P&L": {}
    };
    table.cash[a_title] = A.cash + "$";
    table.cash[b_title] = B.cash + "$";
    table.cash["Total"] = A.cash + B.cash + "$";
    table.demand[a_title] = A.demand;
    table.demand[b_title] = B.demand;
    table.demand["Total"] = A.demand + B.demand;
    table["P&L"][a_title] = a_pnl + '$';
    table["P&L"][b_title] = b_pnl + '$';
    table["P&L"]["Total"] = a_pnl + b_pnl + '$';

    console.table(table)
    console.log('\n');
    console.groupEnd();
    // console.log(`${time}: ${a_pnl} + ${b_pnl} = ${a_pnl + b_pnl}`)
}

