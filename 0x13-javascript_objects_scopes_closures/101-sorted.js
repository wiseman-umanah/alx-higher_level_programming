#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

Object.keys(dict).forEach((key) => {
  const value = dict[key];
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(key);
});

console.log(newDict);
