#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
    if (dict.hasOwnProperty(key)) {
        const value = dict[key];
        if (value in newDict) {
            newDict[value].push(key);
        } else {
            newDict[value] = [key];
        }
    }
}
console.log(newDict);
