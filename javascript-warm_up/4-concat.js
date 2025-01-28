#!/usr/bin/node

const arg1 = process.argv[2]; // No default value (allows `undefined`)
const arg2 = process.argv[3]; 
console.log(`${arg1} is ${arg2}`);
