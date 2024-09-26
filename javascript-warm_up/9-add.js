#!/usr/bin/node
const add = (a, b) => a + b;

const Arg1 = parseInt(process.argv[2]);
const Arg2 = parseInt(process.argv[3]);

console.log(add(Arg1, Arg2));
