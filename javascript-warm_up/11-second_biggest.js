#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  const uniqueNumbers = [];
  for (let i = 0; i < numbers.length; i++) {
    if (uniqueNumbers.indexOf(numbers[i]) === -1) {
      uniqueNumbers.push(numbers[i]);
    }
  }
  uniqueNumbers.sort((a, b) => b - a);

  console.log(uniqueNumbers[1]);
}
