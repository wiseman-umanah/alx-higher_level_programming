#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
	let res = 0;
	for (i in list){
		if (list[i] === searchElement){
			res++;
		}
	}
	return (res);
}

//prolific