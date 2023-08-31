#!/usr/bin/node
const parsed = require('process');
let resp;
let num;
resp = 'Not a number';
if (parsed.argv.length > 2) {
  num = parseInt(parsed.argv[2]);
  if (!isNaN(num)) {
    resp = 'My number: ' + String(num);
  }
}
console.log(resp);