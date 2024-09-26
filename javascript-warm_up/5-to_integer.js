#!/usr/bin/node
const args = process.argv.slice(2);

const Arg1 = args[0];

if (Arg1 !== undefined && ! isNaN(parseInt(Arg1))) {
	console.log("My number:" + " "+parseInt(Arg1));
} else {
	console.log("Not a number");
}
