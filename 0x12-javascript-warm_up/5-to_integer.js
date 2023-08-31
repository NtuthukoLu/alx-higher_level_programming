#!/usr/bin/node
const input = process.argv[2];

const number = parseInt(input);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log("Not a number");
}