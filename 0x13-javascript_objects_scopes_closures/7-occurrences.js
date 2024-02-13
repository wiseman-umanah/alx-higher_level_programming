#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let res = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      res++;
    }
  }
  return (res);
};

// prolific
