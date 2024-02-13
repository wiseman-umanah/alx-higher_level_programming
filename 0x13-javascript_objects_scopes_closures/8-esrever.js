#!/usr/bin/node
exports.esrever = function (list) {
  const dum = [];
  for (let i = list.length - 1; i >= 0; i--) { dum.push(list[i]); }
  list = dum;
  return (list);
};
