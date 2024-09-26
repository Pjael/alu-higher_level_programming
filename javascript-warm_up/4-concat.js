#!/usr/bin/node
const args = process.argv.slice(2);

let Arg1;
let Arg2;

if (args[0] !== undefined) {
  Arg1 = args[0];
} else {
  Arg1 = 'undefined';
}

if (args[0] !== undefined) {
  Arg2 = args[1];
} else {
  Arg2 = 'undefined';
}

console.log(Arg1 + ' ' + 'is' + ' ' + Arg2);
