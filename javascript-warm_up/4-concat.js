#!/usr/bin/node

// Get arguments, defaulting to empty strings if missing
const arg1 = process.argv[2] || '';
const arg2 = process.argv[3] || '';

console.log(`${arg1} is ${arg2}`);
